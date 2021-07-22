from  odoo import http


class Books(http.Controller):
    """
        Class controller to acces the webpage of the rootkit models
    """
    @http.route('/rootkit/books', auth='user')
    def list(self, **kwargs):
        "Function that will list the books on the webpage"
        Book = http.request.env['rootkit.book']
        books = Book.search([])
        return http.request.render(
            'rootkit.book_list_template', {'books': books}
        )
