import rsa
import configparser
import os


def gen_keypair(nbits: int = 128):
    """ Generate New Key Pair """
    pu, pr = rsa.newkeys(nbits)
    return pu, pr


def read_config(filename: str = 'config.ini'):
    config = configparser.ConfigParser()
    if os.path.exists(filename):
        # Handle Exists Config File
        config.read(filename)
    else:
        # Create New Config File
        with open(filename, 'w') as config_file:
            config.write(config_file)
    return config


def main():
    # print(gen_keypair())
    read_config()


if __name__ == '__main__':
    main()