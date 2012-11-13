#!/usr/bin/python
#
# Authors: 'giaba90'
# Email: giaba90@gmail.com 
#
# This file may be licensed under the terms of of the
# GNU General Public License Version 2 (the ``GPL'').
#
# Software distributed under the License is distributed
# on an ``AS IS'' basis, WITHOUT WARRANTY OF ANY KIND, either
# express or implied. See the GPL for the specific language
# governing rights and limitations.
#
# You should have received a copy of the GPL along with this
# program. If not, go to http://www.gnu.org/licenses/gpl.html
# or write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

#generatore di numeri pseudo-casuali con congruenza lineare

class PyRandom:
    def __init__(self):
	self.a=16807 #moltiplicatore
	self.c=0     #incrementatore
	self.m=2147483647 #modulo
    def clock(self):
	from datetime import datetime
	t=datetime.now()
	clock=t.year+t.month+t.day+t.hour+t.second+t.microsecond
	clock=clock%self.m
	return clock
    def random(self,n,seme):
        output=[]
        while len(output)<n: #inizializzo
            output.append(0)
        output[0]=((self.a*seme)+self.c)%self.m  #fase 0
        i=1
        while i<n: 
            output[i]=(((self.a*output[i-1])+self.c)%self.m)+self.clock()
            i=i+1    
	return output 