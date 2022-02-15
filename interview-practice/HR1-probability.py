#given mu, sigma, find p 
#Question 1: p < 40, p > 21, p (30-35) with mu =30, sig=4
#Question 2: p < 19.5, p (20-22) with mu =20, sig=2

def get_table_p(x, mu=20, sig=2):
    z = (x - mu)/sig
    print('z score for',x,'is',z)
    tab_p = 0
    if z == 1:  
        tab_p = 0.8413
    if z == -0.25: 
        tab_p = 0.5987
    if z == 0:
        tab_p = 0.5000 
    return tab_p

def print_p():    
    p_19p5 = 1 - round(get_table_p(19.5),3)
    p_2022 = round(get_table_p(22) - get_table_p(20),3)
    print(p_19p5)
    print(p_2022)

if __name__ == "__main__":
    print_p()

