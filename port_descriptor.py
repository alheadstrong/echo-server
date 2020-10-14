import socket
import sys


def port_descriptions(lower=0, upper=65535):
    for port in range(lower, upper):
        try:
            print("Port {}: {}".format(port, socket.getservbyport(port)))
        except OSError:
            continue


if __name__ == '__main__':
    if len(sys.argv) == 1:
        port_descriptions()
    elif len(sys.argv) == 3:
        try:
            lower_bound = int(sys.argv[1])
            upper_bound = int(sys.argv[2])

            if lower_bound < 0 or lower_bound > 65535:
                usage = """\nlower bound > 0, upper bound < 65535\n"""
                print(usage, file=sys.stderr)
                sys.exit(1)
            else:
                port_descriptions(lower=lower_bound, upper=upper_bound)

        except ValueError:
            usage = """\nenter integers as lower and upper bounds, without commas\n"""
            print(usage, file=sys.stderr)
            sys.exit(1)

    else:
        usage = """\nusage:
                    \nall ports: python port_descriptor 
                    \nrange of ports: python port_descriptor (lower_bound) (upper_bound)\n"""
        print(usage, file=sys.stderr)
        sys.exit(1)
