from pyVoIP.SIP import SIPMessage
import pytest


@pytest.mark.parametrize(
    "packet,expected",
    [
        (
            b"""SIP/2.0 401 Unauthorized\r\nVia: SIP/2.0/UDP 0.0.0.0:5060;branch=z9hG4bK03150189fc65493a9d4e3a582;rport=5060;received=192.168.178.110\r\nFrom: "tarantulla" <sip:tarantulla@192.168.178.1>;tag=9338abd3\r\nTo: "tarantulla" <sip:tarantulla@192.168.178.1>;tag=950C00889AC0DB3B\r\nCall-ID: 6b86b273ff34fce19d6b804eff5a3f57@0.0.0.0:5060\r\nCSeq: 1 REGISTER\r\nWWW-Authenticate: Digest realm="fritz.box", nonce="78B29326485EAE52"\r\nUser-Agent: FRITZ!OS\r\nContent-Length: 0\r\n\r\n""",
            {"realm": "fritz.box", "nonce": "78B29326485EAE52"},
        ),
        (
            b"""SIP/2.0 401 Unauthorized\r\nVia: SIP/2.0/UDP 0.0.0.0:5060;branch=z9hG4bK03150189fc65493a9d4e3a582;rport=5060;received=192.168.178.110\r\nFrom: "tarantulla" <sip:tarantulla@192.168.178.1>;tag=9338abd3\r\nTo: "tarantulla" <sip:tarantulla@192.168.178.1>;tag=950C00889AC0DB3B\r\nCall-ID: 6b86b273ff34fce19d6b804eff5a3f57@0.0.0.0:5060\r\nCSeq: 1 REGISTER\r\nWWW-Authenticate: Digest algorithm=MD5,realm="local",nonce="111111:222222aaaaaa333333bbbbbb444444"\r\nUser-Agent: FRITZ!OS\r\nContent-Length: 0\r\n\r\n""",
            {
                "algorithm": "MD5",
                "realm": "local",
                "nonce": "111111:222222aaaaaa333333bbbbbb444444",
            },
        ),
        (
            b"""SIP/2.0 401 Unauthorized\r\nVia: SIP/2.0/UDP 0.0.0.0:5060;branch=z9hG4bK03150189fc65493a9d4e3a582;rport=5060;received=192.168.178.110\r\nFrom: "tarantulla" <sip:tarantulla@192.168.178.1>;tag=9338abd3\r\nTo: "tarantulla" <sip:tarantulla@192.168.178.1>;tag=950C00889AC0DB3B\r\nCall-ID: 6b86b273ff34fce19d6b804eff5a3f57@0.0.0.0:5060\r\nCSeq: 1 REGISTER\r\nWWW-Authenticate: Digest algorithm=MD5, realm="asterisk",nonce="45f77cee"\r\nUser-Agent: FRITZ!OS\r\nContent-Length: 0\r\n\r\n""",
            {
                "algorithm": "MD5",
                "realm": "asterisk",
                "nonce": "45f77cee",
            },
        ),
        (
            b"""SIP/2.0 401 Unauthorized\r\nVia: SIP/2.0/UDP 192.168.0.76:5060;rport=5060;received=192.168.0.76;branch=z9hG4bK92b19bf363d84d2ea95d18cd3\r\nCall-ID: 6b86b273ff34fce19d6b804eff5a3f57@192.168.0.76:5060\r\nFrom: "5555" <sip:5555@192.168.0.100>;tag=fb11549a\r\nTo: "5555" <sip:5555@192.168.0.100>;tag=z9hG4bK92b19bf363d84d2ea95d18cd3\r\nCSeq: 1 REGISTER\r\nWWW-Authenticate: Digest realm="asterisk",nonce="1664256201/30ff48bd45c78b935077262030d584bd",opaque="5f0937be1ccec4cf",algorithm=md5,qop="auth"\r\nServer: Asterisk PBX 18.2.0\r\nContent-Length:  0\r\n\r\n""",
            {
                "algorithm": "md5",
                "realm": "asterisk",
                "nonce": "1664256201/30ff48bd45c78b935077262030d584bd",
                "opaque": "5f0937be1ccec4cf",
                "qop": "auth",
            },
        ),
    ],
)
def test_sip_authentication(packet, expected):
    message = SIPMessage(packet)
    assert message.authentication == expected


@pytest.mark.parametrize(
    "packet,expected",
    [
        (
            b"""SIP/2.0 401 Unauthorized\r\nVia: SIP/2.0/UDP 0.0.0.0:5060;branch=z9hG4bK03150189fc65493a9d4e3a582;rport=5060;received=192.168.178.110\r\nFrom: "tarantulla" <sip:tarantulla@192.168.178.1>;tag=9338abd3\r\nTo: "tarantulla" <sip:tarantulla@192.168.178.1>;tag=950C00889AC0DB3B\r\nCall-ID: 6b86b273ff34fce19d6b804eff5a3f57@0.0.0.0:5060\r\nCSeq: 1 REGISTER\r\nWWW-Authenticate: Digest realm="fritz.box", nonce="78B29326485EAE52"\r\nUser-Agent: FRITZ!OS\r\nContent-Length: 0\r\n\r\n""",
            {
                "raw": '"tarantulla" <sip:tarantulla@192.168.178.1>;tag=950C00889AC0DB3B',
                "tag": "950C00889AC0DB3B",
                "uri": "sip:tarantulla@192.168.178.1",
                "uri-type": "sip",
                "user": "tarantulla",
                "password": "",
                "display-name": "tarantulla",
                "host": "192.168.178.1",
                "port": 5060,
            },
        ),
        (
            b"""SIP/2.0 401 Unauthorized\r\nVia: SIP/2.0/UDP 192.168.0.76:5060;rport=5060;received=192.168.0.76;branch=z9hG4bK92b19bf363d84d2ea95d18cd3\r\nCall-ID: 6b86b273ff34fce19d6b804eff5a3f57@192.168.0.76:5060\r\nFrom: "5555" <sip:5555@192.168.0.100>;tag=fb11549a\r\nTo: "5555" <sip:5555@192.168.0.100>;tag=z9hG4bK92b19bf363d84d2ea95d18cd3\r\nCSeq: 1 REGISTER\r\nWWW-Authenticate: Digest realm="asterisk",nonce="1664256201/30ff48bd45c78b935077262030d584bd",opaque="5f0937be1ccec4cf",algorithm=md5,qop="auth"\r\nServer: Asterisk PBX 18.2.0\r\nContent-Length:  0\r\n\r\n""",
            {
                "raw": '"5555" <sip:5555@192.168.0.100>;tag=z9hG4bK92b19bf363d84d2ea95d18cd3',
                "tag": "z9hG4bK92b19bf363d84d2ea95d18cd3",
                "uri": "sip:5555@192.168.0.100",
                "uri-type": "sip",
                "user": "5555",
                "password": "",
                "display-name": "5555",
                "host": "192.168.0.100",
                "port": 5060,
            },
        ),
        (
            b"""SIP/2.0 401 Unauthorized\r\nVia: SIP/2.0/UDP 192.168.0.76:5060;rport=5060;received=192.168.0.76;branch=z9hG4bK92b19bf363d84d2ea95d18cd3\r\nCall-ID: 6b86b273ff34fce19d6b804eff5a3f57@192.168.0.76:5060\r\nFrom: "5555" <sip:5555@192.168.0.100>;tag=fb11549a\r\nTo: "5555" <sip:5555:secret_password@192.168.0.100:616>;tag=z9hG4bK92b19bf363d84d2ea95d18cd3\r\nCSeq: 1 REGISTER\r\nWWW-Authenticate: Digest realm="asterisk",nonce="1664256201/30ff48bd45c78b935077262030d584bd",opaque="5f0937be1ccec4cf",algorithm=md5,qop="auth"\r\nServer: Asterisk PBX 18.2.0\r\nContent-Length:  0\r\n\r\n""",
            {
                "raw": '"5555" <sip:5555:secret_password@192.168.0.100:616>;tag=z9hG4bK92b19bf363d84d2ea95d18cd3',
                "tag": "z9hG4bK92b19bf363d84d2ea95d18cd3",
                "uri": "sip:5555@192.168.0.100:616",
                "uri-type": "sip",
                "user": "5555",
                "password": "secret_password",
                "display-name": "5555",
                "host": "192.168.0.100",
                "port": 616,
            },
        ),
        (
            b"""SIP/2.0 401 Unauthorized\r\nVia: SIP/2.0/UDP 192.168.0.76:5060;rport=5060;received=192.168.0.76;branch=z9hG4bK92b19bf363d84d2ea95d18cd3\r\nCall-ID: 6b86b273ff34fce19d6b804eff5a3f57@192.168.0.76:5060\r\nFrom: "5555" <sip:5555@192.168.0.100>;tag=fb11549a\r\nTo: "5555" <sip:5555:secret_password@192.168.0.100>;tag=z9hG4bK92b19bf363d84d2ea95d18cd3\r\nCSeq: 1 REGISTER\r\nWWW-Authenticate: Digest realm="asterisk",nonce="1664256201/30ff48bd45c78b935077262030d584bd",opaque="5f0937be1ccec4cf",algorithm=md5,qop="auth"\r\nServer: Asterisk PBX 18.2.0\r\nContent-Length:  0\r\n\r\n""",
            {
                "raw": '"5555" <sip:5555:secret_password@192.168.0.100>;tag=z9hG4bK92b19bf363d84d2ea95d18cd3',
                "tag": "z9hG4bK92b19bf363d84d2ea95d18cd3",
                "uri": "sip:5555@192.168.0.100",
                "uri-type": "sip",
                "user": "5555",
                "password": "secret_password",
                "display-name": "5555",
                "host": "192.168.0.100",
                "port": 5060,
            },
        ),
        (
            b"""SIP/2.0 401 Unauthorized\r\nVia: SIP/2.0/UDP 192.168.0.76:5060;rport=5060;received=192.168.0.76;branch=z9hG4bK92b19bf363d84d2ea95d18cd3\r\nCall-ID: 6b86b273ff34fce19d6b804eff5a3f57@192.168.0.76:5060\r\nFrom: "5555" <sip:5555@192.168.0.100>;tag=fb11549a\r\nTo: "5555" <sip:5555@192.168.0.100:616>;tag=z9hG4bK92b19bf363d84d2ea95d18cd3\r\nCSeq: 1 REGISTER\r\nWWW-Authenticate: Digest realm="asterisk",nonce="1664256201/30ff48bd45c78b935077262030d584bd",opaque="5f0937be1ccec4cf",algorithm=md5,qop="auth"\r\nServer: Asterisk PBX 18.2.0\r\nContent-Length:  0\r\n\r\n""",
            {
                "raw": '"5555" <sip:5555@192.168.0.100:616>;tag=z9hG4bK92b19bf363d84d2ea95d18cd3',
                "tag": "z9hG4bK92b19bf363d84d2ea95d18cd3",
                "uri": "sip:5555@192.168.0.100:616",
                "uri-type": "sip",
                "user": "5555",
                "password": "",
                "display-name": "5555",
                "host": "192.168.0.100",
                "port": 616,
            },
        ),
        # Begin RFC Examples
        (
            b"""SIP/2.0 200 OK\r\nTo: The Operator <sip:operator@cs.columbia.edu>;tag=287447\r\n\r\n""",
            {
                "raw": "The Operator <sip:operator@cs.columbia.edu>;tag=287447",
                "tag": "287447",
                "uri": "sip:operator@cs.columbia.edu",
                "uri-type": "sip",
                "user": "operator",
                "password": "",
                "display-name": "The Operator",
                "host": "cs.columbia.edu",
                "port": 5060,
            },
        ),
        (
            b"""SIP/2.0 200 OK\r\nt: sip:+12125551212@server.phone2net.com\r\n\r\n""",
            {
                "raw": "sip:+12125551212@server.phone2net.com",
                "tag": "",
                "uri": "sip:+12125551212@server.phone2net.com",
                "uri-type": "sip",
                "user": "+12125551212",
                "password": "",
                "display-name": "",
                "host": "server.phone2net.com",
                "port": 5060,
            },
        ),
    ],
)
def test_sip_to_from(packet, expected):
    message = SIPMessage(packet)
    assert type(message.headers["To"]) == dict
    assert message.headers["To"] == expected
