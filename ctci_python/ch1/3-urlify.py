def urlify(url):
	url = url.strip()
	to_url = ""

	for i in range(0,len(url)):
		if url[i] == " ":
			if url[i-1] != " ":
				to_url += "%20"
		else:
			to_url += url[i]

	print(to_url)
	return to_url

str1 = "Tabby Cat Website"
str2 = "Spaces         Yeah"
str3 = "Weirdo       A "

urlify(str1)
urlify(str2)
urlify(str3)