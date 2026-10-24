import math

def poisson_probability(k, lam):
	# formula for poisson distrubution given as p(k) = lam^k.e^-lam/k!  lam = the mean rate of occurence k = the exact number of events you want to observe e = euler number mathematical constanst 0.0067379   poisson distribution is a discrete probability distribution that calculates the likelyhood of a certain number of events occuring within a fixed interval of time
	lam_k = lam ** k
	euler_lam = math.exp(-lam)
	k_fact = math.factorial(k)
	val = (lam_k * euler_lam) / k_fact
	return round(val,5)