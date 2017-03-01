import graphene

class Query(graphene.ObjectType):
    hello = graphene.String()

    def resolve_hello(self, args, context, info):
        return 'Hello worlds!'

schema = graphene.Schema(query=Query)

# Testing
query = '''
query something{
    hello
}
'''

def test_query():
    result = schema.execute(query)
    assert not result.errors
    assert result.data == {
        'hello': 'Hello worlds!'
    }

if __name__ == '__main__':
    result = schema.execute(query)
    print(result.data['hello'])