"""
handling completely dynamic element:
------------------------------------
*an element is completely changing then it is called as completely dynamic element.
*we can handle in 2 ways,
1.xpath by traversing

1.xpath by traversing:
======================
*navigating from one element to another element is called as traversing.
*traversing is classified into 2 types,
1.forward traversing
2.backward traversing

1.forward traversing:
---------------------
*navigating from parent to child element by using / (or) // is called as forward traversing.

2.backward traversing:
----------------------
*navigating from child to parent element by using /.. (or) //ancestor is called as backward traversing.

how to handle completely dynamic element:
=========================================
step1: inspect static element 
step2: navigate from static element to common parent(common parent means it should be a parent of
both static and dynamic element)
step3: navigate from common parent to dynamic element

xpath to inspect collection of pushpa movie
(//td[.='Pushpa']/../td)[4]

xpath to inspect review of kgf movie
(//td[.='KGF']/../td)[5]

xpath to inspect sl.no of RRR movie
(//td[.='RRR']/..//td)[1]

xpath to inspect version of python
(//p[.='Python']/..//a)[1]
"""
#sample html code of movie table
"""
<html>
          <body bgcolor="pink">
	<table border=3>
	             <tr>
		<td>sl.no</td>
		<td>certificate</td>
		<td>movie name</td>
		<td>collection</td>
		<td>ratings</td>		
                                  </tr>
	             <tr>
		<td>1</td>
		<td>U/A</td>
		<td>KGF</td>
		<td>50CR</td>
		<td>****</td>		
                                  </tr>
	             <tr>
		<td>2</td>
		<td>U</td>
		<td>Kantara</td>
		<td>500CR</td>
		<td>*****</td>		
                                  </tr>
	             <tr>
		<td>3</td>
		<td>U/A</td>
		<td>RRR</td>
		<td>80CR</td>
		<td>***</td>		
                                  </tr>
	             <tr>
		<td>4</td>
		<td>A</td>
		<td>Dhoom</td>
		<td>5CR</td>
		<td>**</td>		
                                  </tr>
      	</table>
          </body>
</html>
"""
