from rest_framework.response import Response


def response_bs(self, code, status, message):
    return Response(
        {
            "code": code,
            "status": status,
            "message": message
        }
    )


def response(self, code, status, message, serializer):
    return Response(
        {
            "code": code,
            "status": status,
            "message": message,
            "data": serializer.data
        }
    )

def response_login(self, code, status, message, serializer, token):
    return Response({
        "code": code,
            "status": status,
            "message": message,
            "token": token,
            "data": serializer.data
    })