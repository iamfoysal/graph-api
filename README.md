###### create and run the migrations for our database:

     $ python manage.py makemigrations
     $ python manage.py migrate
     
  
 ###### run demo data the command below to import the data into the database:
    
      $ python manage.py loaddata data.json
 
 
 The ``CreateBook`` class will be used to create and save new `Book` entries to the database. For every mutation class we must have an ``Arguments`` inner class and a ``mutate()`` class method.

We defined an instance of the ``BookInput`` class we created earlier as our arguments, and we made it mandatory with the ``required=True`` option. After that we defined the model we are working with by doing this ``book = graphene.Field(BookType)``.

In the ``mutate`` method we are saving a new book by calling the ``save()`` method on a new ``Book`` instance created from the ``book_data`` values passed as argument.

Below you can see the implementation of the ``UpdateBook`` mutation. Add this code at the bottom of ``api/schema.py``:

  class UpdateBook(graphene.Mutation):
    class Arguments:
        book_data = BookInput(required=True)

    book = graphene.Field(BookType)

    @staticmethod
    def mutate(root, info, book_data=None):

        book_instance = Book.objects.get(pk=book_data.id)

        if book_instance:
            book_instance.title = book_data.title
            book_instance.author = book_data.author
            book_instance.year_published = book_data.year_published
            book_instance.review = book_data.review
            book_instance.save()

            return UpdateBook(book=book_instance)
        return UpdateBook(book=None)
        
######  Let’s start the Django server:
   
          $ python manage.py runserver
          
Now visit ``http://127.0.0.1:8000/api/graphql`` in your browser. You should see the GraphIQL interface for interactive testing of the GraphQL API. 


##### Issuing a query

       query {
              allBooks {
                id
                title
                author
                yearPublished
                review
              }
            }

The GraphQL code below is requesting all the books from the database

###### For single query following the query, which requests a single book by its id:

          query {
            book(bookId: 2) {
                   id
                   title
                   author
                 }
               }


##### for create new Book. GraphQL snippet defines a mutation that adds a new book to the database: 

          mutation createMutation {
            createBook(bookData: {title: "The Chronicles", author: "Jhon Deo", yearPublished: "1980", review: 42}) {
              book {
                title,
                author,
                yearPublished,
                review
              }
            }
          }

##### The next GraphQL mutation updates the book with id=5:

          mutation updateMutation {
            updateBook(bookData: {id: 5, title: "The Lord of the Rings", author: "J.J.R", yearPublished: "1948", review: 20}) {
              book {
                title,
                author,
                yearPublished,
                review
              }
            }
          }
          
##### The final mutation example deletes the book with id=4 from the database: 

          mutation deleteMutation{
            deleteBook(id: 6) {
              book {
                id
              } 
            }
          }

               
               



      
