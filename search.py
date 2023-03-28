import json

class Search:

    def __init__(self, req):
        self.req = req
        self.result = self.search(self.req)
        
    def search(self, req):
        
        with open('Data/books.json') as f:
            data = json.load(f)
            
            r = []
            count = 0
            for book in data:
                if(req in book["title"] or req.capitalize() in book["title"]) :
                    r.append(book["author"] + " - " + book["title"])
                    count+=1
                elif(req in book["author"] or req.capitalize() in book["author"]):
                    r.append(book["author"] + " - " + book["title"])
                    count += 1
            if(count == 0): 
                return "No results found"
            return r
        