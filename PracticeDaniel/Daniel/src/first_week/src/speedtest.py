from speedtest import Speedtest
import pprint
def test_connection():
        speedtest.Speedtest()
        s.get_servers()
        s.get_best_server()
        s.download()
        s.upload()

    return speedtest.results.dic()

if __name__== '__main'