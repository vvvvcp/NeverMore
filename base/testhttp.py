import argparse
from lib.simple_http import CustomHTTPServer


DEFAULT_HOST='127.0.0.1'
DEFAULT_PORT=8800

def run_server(port):
    try:
        server= CustomHTTPServer(DEFAULT_HOST, port)
        print "Custom HTTP server started on port: %s" % port
        server.serve_forever()
    except Exception, err:
        print "Error:%s" %err
    except KeyboardInterrupt:
        print "Server interrupted and is shutting down..."
        server.socket.close()
        
        
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Simple HTTP Server Example')
    parser.add_argument('--port',action='store',dest='port',type=int,default=DEFAULT_PORT)
    given_args =parser.parse_args()
    port=given_args.port
    run_server(port)

