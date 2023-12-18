import time
import json
from ricxappframe.xapp_frame import Xapp
from ricxappframe.service import kpimon


def entry(self):
    my_ns = "ns1"
    number = 0

    while True:
        # test healthcheck
        print("xapp is healthy? {}".format(xapp.healthcheck()))

        msg = kpimon.recv(4096)
        # rmr send to default handler
        self.rmr_send(json.dumps({"kpi": msg}).encode(), 6660666)

        val = json.dumps({"kpi": msg}).encode()
        self.rmr_send(val, 60000)


        # rmr receive
        for (summary, sbuf) in self.rmr_get_messages():
            self.rmr_free(sbuf)

        time.sleep(2)


xapp = Xapp(entrypoint=entry, rmr_port=4564, use_fake_sdl=True)
config = json.loads(pathlib.Path(args.ric_config).read_text())
e2_client = Xapp.E2Client(**config["e2_client"])
kpimon.subsribe(e2_client)
xapp.run()