'''
handling partially dynamic element:
-----------------------------------

*in an element some portion is static and some portion is dynamic is called as partially
dynamic element.
*to handle partially dynamic element we use contains().

when to go contains() function?
-------------------------------
*to handle partially dynamic element.
*if text value/attribute value is very lengthy.
*if text value begins/ends with spaces.

contains with attribute syntax:
-------------------------------
//tagname[contains(@attribute_name , 'attribute_value')]

contains with text:
-------------------
//tagname[contains(. , 'text_value')]

xpath to inspect windows version
(//span[contains(., 'Get Windows')])[1]

xpath to inspect python version in python.org
(//a[contains(., 'Download Python')])[2]

xpath to inspect fruits and vegetables in zepto
(//span[contains(@class , 'Label-sc-15v1nk5-0')])[9]

xpath to inspect mobile in amazon
//a[contains(@href, '/mobile-phones/')]

xpath to inspect power bank in dunnzo
//h5[contains(., '20000 mAh')]

xpath to inspect admissions in jain.com
(//a[contains(., 'Admissions')])[3]

xpath to inspect books in demo webshop
(//a[contains(.,'Books')])[1]
"""

'''