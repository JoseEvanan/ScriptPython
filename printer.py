from escpos.connections import getNetworkPrinter


printer = getNetworkPrinter()(host='192.168.0.137', port=213)

printer.text("Hello World")
printer.lf()