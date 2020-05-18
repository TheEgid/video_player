from livereload import Server, shell


server = Server()
server.watch('/*.html', shell('make html', cwd='docs'))
server.serve(root='.')

#http://flexbox.help/
