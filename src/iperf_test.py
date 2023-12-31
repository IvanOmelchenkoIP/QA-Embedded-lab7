import iperf_parser


class TestSuite:
    def test_iperf3_client_connection(self, client):
        stdout, error, error_serv = client
        assert not error_serv
        assert not error
        dict = iperf_parser.parser(stdout)
        for value in dict:
            transfer = float(value["Transfer"])
            bitrate = float(value["Bitrate"])
            assert transfer > 5 and bitrate > 50
