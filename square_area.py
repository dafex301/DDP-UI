import matplotlib.pyplot as plt

# Trapezoidal Method

# Define function to integrate
def f(x):
    return 2 +13*x**6+8*x**3

# Implementing trapezoidal method
def trapezoidal(x0,xn,n):
    # calculating step size
    h = (xn - x0) / n
    
    # Finding sum 
    integration = f(x0) + f(xn)
    
    for i in range(1,n):
        k = x0 + i*h
        integration = integration + 2 * f(k)
    
    # Finding final integration value
    integration = integration * h/2
    
    return integration
    
# Input section
lower_limit = float(input("Masukkan batas bawah dari integral: "))
upper_limit = float(input("Masukkan batas atas integral: "))
sub_interval = [10, 50, 100, 500, 1000]

# Call trapezoidal() method and get result
error_array = list()
for i in sub_interval:
  result = trapezoidal(lower_limit, upper_limit, i)
  print("\nIntegration result by Trapezoidal method is: %0.6f" % (result))

  exact_intgr = (2*upper_limit+13/7*upper_limit**7+2*upper_limit**4)-(2*lower_limit+13/7*lower_limit**7+2*lower_limit**4)

  print("Hasil definite integralnya adalah: %0.1f" % (exact_intgr))

  error = (exact_intgr - result)/exact_intgr*100
  error_array.append(abs(error))
  print("N="+str(i))
  print("Error yang dialami fungsi f(x) saat menghitung dengan menggunakan Trapezoidal Method dan Definite Integral adalah  " +str(round(abs(error), 5))+"%")

plt.plot(sub_interval, error_array)
plt.title('Jumlah N vs Persentase Error')
plt.xlabel('Jumlah N')
plt.ylabel('Persentase Error')
plt.show()