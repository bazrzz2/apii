 
    def handleRequest(self):
        try:
         
           data = """<script>
console.log("gg")

</script>"""
       self.wfile.write(data)
