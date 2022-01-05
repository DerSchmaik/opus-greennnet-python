from opus_grennnet import OPUSAPI, Auth

def main():
    auth = Auth('http://192.168.178.88:8080', '082D3EB')
    opus = OPUSAPI(auth)

    

main()