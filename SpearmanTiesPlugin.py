import sys
#import numpy
import PyPluMA
import math
import scipy.stats

class SpearmanTiesPlugin:
   def input(self, filename):
      self.myfile = filename

   def run(self):
      filestuff = open(self.myfile, 'r')
      self.firstline = filestuff.readline()
      self.bacteria = self.firstline.split(',')
      if (self.bacteria.count('\"\"') != 0):
         self.bacteria.remove('\"\"')
      print self.bacteria
      self.n = len(self.bacteria)
      self.ADJ = []
      i = 0
      print self.n
      for line in filestuff:
         contents = line.split(',')
	 self.ADJ.append([])
         for j in range(self.n):
            value = float(contents[j+1])
            self.ADJ[i].append(value)
         i += 1
      self.m = len(self.ADJ)

   def output(self, filename):
      averages = []
      vecs = []
      for j in range(self.n):
         mysum = 0.0
         vecs.append([])
         for i in range(self.m):
            mysum += self.ADJ[i][j]
            vecs[j].append(self.ADJ[i][j])
         averages.append(mysum / self.m)

      corr = []
      for k in range(self.n):
         corr.append([])
         for j in range(self.n):
            corr[k].append(0.0)

      for k in range(self.n):
         corr.append([])
         for j in range(self.n):
            if (k == j):
               corr[k][j] = 1
            else:
               sum_num = 0.0
               sum_denom_x = 0.0
               sum_denom_y = 0.0
               for i in range(self.m):
                  sum_num += (self.ADJ[i][k] - averages[k])*(self.ADJ[i][j] - averages[j])
                  sum_denom_x += (self.ADJ[i][k] - averages[k])**2
                  sum_denom_y += (self.ADJ[i][j] - averages[j])**2
               if (sum_num == 0):
                  corr[k][j] = 0
               else:
                  corr[k][j] = sum_num / math.sqrt(sum_denom_x * sum_denom_y) 
                  if (abs(corr[k][j]) < 1):
                     pval = 2*scipy.stats.norm.cdf(-abs(math.sqrt((self.m-3)/1.06)*math.atanh(corr[k][j])))
                     if (pval > 0.05):
                        corr[k][j] = 0

      filestuff2 = open(filename, 'w')
      self.firstline = self.firstline.replace("\"\",", "")
      filestuff2.write(self.firstline)

      for i in range(self.n):
         filestuff2.write(self.bacteria[i].strip()+',')
         for j in range(self.n):
            filestuff2.write(str(corr[i][j]))
            if (j < self.n-1):
               filestuff2.write(",")
            else:
               filestuff2.write("\n")



