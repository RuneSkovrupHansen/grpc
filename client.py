import grpc

import mmo_pb2
import mmo_pb2_grpc


def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = mmo_pb2_grpc.MMOServiceStub(channel)

        # Point is generated at import time from the embedded descriptor in
        # mmo_pb2.py. Building it is local; the RPC happens in stub.GetZone(...).
        response = stub.GetZone(mmo_pb2.Point(latitude=51, longitude=12))
        print("Zone:", response.name)


if __name__ == "__main__":
    run()
