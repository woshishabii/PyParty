import rsa
import configparser
import os


def get_keypair(nbits: int = 128):
    """ Generate New Key Pair """
    if os.path.exists('private.pem') and os.path.exists('public.pem'):
        # Read exists Key Pair
        with open('private.pem', 'rb+') as f_pr, open('public.pem', 'rb+') as f_pu:
            pr = rsa.PrivateKey.load_pkcs1(f_pr.read())
            pu = rsa.PublicKey.load_pkcs1(f_pu.read())
        print('[LOG] Key Pair Load Successfully')
    else:
        # Generate New Key Pair
        print('[LOG] Key Pair Does Not Exist, Generating a new one')
        pu, pr = rsa.newkeys(nbits)
        with open('private.pem', 'wb+') as f_pr, open('public.pem', 'wb+') as f_pu:
            f_pr.write(pr.save_pkcs1())
            f_pu.write(pu.save_pkcs1())
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
    read_config()
    get_keypair(128)


if __name__ == '__main__':
    main()