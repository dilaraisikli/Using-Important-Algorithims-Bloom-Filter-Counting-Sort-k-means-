import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
style.use('ggplot')

class KMeans:
	def __init__(self, k =3, trashold = 0.0001, maxNumIterations = 500):
		self.k = k  #number of clusters
		self.trashold = trashold
		self.maxNumIterations = maxNumIterations #number of maximum iteration

	def fitCentroids(self, data, mode):#reate and modify the centroids to fit them to the real centroids
		self.centroids = {}

		#initialize the centroids:
		if mode=='w':
		# wrong point: 21 iterations

			self.centroids[0]=np.array([10.00, 10.10])
			self.centroids[1]=np.array([10.00, 13.50])
			self.centroids[2]=np.array([10.00, 15.00])

		elif mode=='b':
		#best point: 7 iterations
			self.centroids[0]=np.array([12.00, 20.10])
			self.centroids[1]=np.array([13.00, 20.50])
			self.centroids[2]=np.array([14.00, 20.00])



		for component in data:
			plt.scatter(component[0], component[1], color = 'black',s = 30)

		for centroid in self.centroids:
			print(self.centroids[centroid][0], self.centroids[centroid][1])
			plt.scatter(self.centroids[centroid][0], self.centroids[centroid][1], s = 300, marker = "*", color='b')
		plt.title('Inizial condition')
		plt.show()

		#begin iterations
		iter=0
		for i in range(self.maxNumIterations):
			self.clusters = {}
			for i in range(self.k):
				self.clusters[i] = []

			#find the distance between the point and cluster; choose the nearest centroid
			for component in data:
				distances = [np.linalg.norm(component - self.centroids[centroid]) for centroid in self.centroids]
				classification = distances.index(min(distances))
				self.clusters[classification].append(component)

			previous = dict(self.centroids)
			#average the cluster datapoints to re-calculate the centroids
			for cluster in self.clusters:
				av=np.average(self.clusters[cluster], axis = 0)
				self.centroids[cluster] = av#np.average(self.clusters[cluster], axis = 0)

			isOptimal = True

			for centroid in self.centroids:

				originalCentroid = previous[centroid]
				current = self.centroids[centroid]

				if np.sum((current - originalCentroid)/originalCentroid * 100.0) > self.trashold:
					isOptimal = False

			colors = 10*["r", "g", "c"]

			for cluster in self.clusters:
				color = colors[cluster]
				for component in self.clusters[cluster]:
					plt.scatter(component[0], component[1], color = color,s = 30)

			for centroid in self.centroids:
				print(self.centroids[centroid])
				plt.scatter(self.centroids[centroid][0], self.centroids[centroid][1], s = 300, marker = "*", color='b')
			plt.title('Iteration {}'.format(iter))
			plt.show()

			#break out of the main loop if the results are optimal, ie. the centroids don't change their positions much(more than our trashold)
			if isOptimal:
				break
			iter+=1
	def pred(self, data):
		distances = [np.linalg.norm(data - self.centroids[centroid]) for centroid in self.centroids]
		classification = distances.index(min(distances))
		return classification

def main(mode):

	df = pd.read_csv(r"wine_try(copia).csv")
	df = df[['b', 'e']]
	dataset = df.astype(float).values.tolist()

	X = df.values #returns a numpy array

	myKeyMeans = KMeans(3)
	myKeyMeans.fitCentroids(X, mode)

	# Plotting starts here
	colors = 10*["r", "g", "c"]

	for cluster in myKeyMeans.clusters:
		color = colors[cluster]
		for component in myKeyMeans.clusters[cluster]:
			plt.scatter(component[0], component[1], color = color,s = 30)

	for centroid in myKeyMeans.centroids:
		plt.scatter(myKeyMeans.centroids[centroid][0], myKeyMeans.centroids[centroid][1], s = 300, marker = "*", color='#050505')
	plt.title('Finish')
	plt.show()

if __name__ == "__main__":
	mode=input('Give me a mode (w for worst; b for best): ')
	main(mode)
