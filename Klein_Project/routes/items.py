from klein import Klein

app = Klein()

@app.route('/items')
def items(request):
    return 'Items route!'
