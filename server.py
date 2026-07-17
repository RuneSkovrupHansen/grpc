from concurrent import futures

import grpc

import mmo_pb2
import mmo_pb2_grpc


class MMOServicer(mmo_pb2_grpc.MMOServiceServicer):
    """Concrete implementation of the MMOService."""

    def GetZone(self, request, context):
        # request is a mmo_pb2.Point; return a mmo_pb2.Zone.
        name = f"zone-{request.latitude}-{request.longitude}"
        return mmo_pb2.Zone(name=name)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    mmo_pb2_grpc.add_MMOServiceServicer_to_server(MMOServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Server listening on :50051")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
