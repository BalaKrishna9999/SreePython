
def totalcostofbasket(pricesfile, basketfile):

    try:
        try:
            pricefl = open(pricesfile, "r")
            prc = (pricefl.readlines())
        except FileNotFoundError:
            print(pricesfile + " does not exist")
        finally:
            pricefl.close()

        try:
            basketfl = open(basketfile, "r")
            bskt = (basketfl.readlines())
        except FileNotFoundError:
            print(basketfile + " does not exist")
        finally:
            basketfl.close()

        for item in prc:
            prcitem = item.split()
            prdtnm = prcitem[0]
            prdcost = int(prcitem[1])
            for itm in bskt:
                productinfo = itm.split()
                productname = productinfo[0]
                productqunty = str(productinfo[1])
                value = int(productqunty[0])
                #qntvar= [int(s) for s in productqunty if s.isdigit()]
                if prdtnm == productname:
                    eachprdctcost = prdcost * value
                    otput = "Cost of  {} {} will be : {}"
                    print(otput.format(productqunty, productname, eachprdctcost))
                    break
    except Exception as ex:
        print("Error" + str(ex))


totalcostofbasket("c:\\Bala\\prices.txt", "c:\\Bala\\basket.txt")
