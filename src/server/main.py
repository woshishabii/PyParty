import pp_socketserver
import pp_request_handler
import pp_config


def main():
    config = pp_config.BasicConfig()
    config.data['Address'] = {}
    config.data['Address']['host'] = '0.0.0.0'
    config.data['Address']['port'] = '9999'
    config.save()
    HOST = config.data['Address']['host']
    PORT = int(config.data['Address']['port'])
    with pp_socketserver.BasicSocketServer((HOST, PORT), pp_request_handler.BasicRequestHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()


if __name__ == '__main__':
    main()