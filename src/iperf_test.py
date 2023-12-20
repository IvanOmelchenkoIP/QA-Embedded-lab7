import iperf_parser


class TestSuite:
    def test_iperf3_client_connection(self, client):
        stdout, error, error_serv = client
        res = "Result from client " + stdout
        print(res)
        assert not error
        assert not error_serv
        dict = iperf_parser.parser(stdout)
        assert len(dict)
        for value in dict:
            transfer = float(value["Transfer"])
            bitrate = float(value["Bitrate"])
            assert transfer > 5 and bitrate > 50
