import json
from ricxappframe.xapp_frame import RMRXapp, rmr, e2rc
import random


def post_init(_self):
    """post init"""
    print("sec xapp")

def isbad(kpm_msg):
# for test only
    if random.randint(1,10)<5:
        return True
    return False

def sec(self, summary, sbuf):
    jpay = json.loads(summary[rmr.RMR_MS_PAYLOAD])
    if isbad(jpay):
        e2rc.send("DISABLE_ADAPTIVE_MCS".encode())
    self.rmr_free(sbuf)


def defh(self, summary, sbuf):
    """callback"""
    print("sec default handler received: {0}".format(summary))
    self.rmr_free(sbuf)


xapp = RMRXapp(default_handler=defh, post_init=post_init, use_fake_sdl=True)
xapp.register_callback(sec, 60000)
config = json.loads(pathlib.Path(args.ric_config).read_text())
e2_client = Xapp.E2Client(**config["e2_client"])
e2rc.connect(e2_client)
xapp.run()