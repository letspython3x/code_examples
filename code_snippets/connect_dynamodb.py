from boto3 import resource

from boto3.dynamodb.conditions import Attr


endpoint_url = r"http://localhost:8000"
table_wcu = 2000
table_rcu = 2000
index_wcu = 3000
index_rcu = 2000



def create_quotation_item():
    db = resource('dynamodb', endpoint_url=endpoint_url)
    table = db.create_table(
        TableName="QuotationItem",
        KeySchema=[
            {
                'AttributeName': '_id',
                'KeyType': 'HASH'
            }],
        AttributeDefinitions=[{'AttributeName': '_id', 'AttributeType': 'S'}],
        ProvisionedThroughput={
            'ReadCapacityUnits': 100,
            'WriteCapacityUnits': 100
        })

    print("Quotation Item Table status:", table.table_status)
    # Wait until the table exists.
    table.meta.client.get_waiter('table_exists').wait(TableName='QuotationItem')

    # Print out some data about the table.
    print(table.item_count)


def create_item_table():
    db = resource('dynamodb', endpoint_url=endpoint_url)
    table = db.create_table(
        TableName="Item",
        KeySchema=[
            {
                "AttributeName": "item_id",
                "KeyType": "HASH"
            },
            {
                "AttributeName": "item_price",
                "KeyType": "RANGE"
            }
        ],
        AttributeDefinitions=[
            {
                "AttributeName": "item_id",
                "AttributeType": "N"
            },
            {
                "AttributeName": "item_price",
                "AttributeType": "S"
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 100,
            'WriteCapacityUnits': 100
        }
    )
    print("Item Table status:", table.table_status)
    # Wait until the table exists.
    table.meta.client.get_waiter('table_exists').wait(TableName="Item")
    # Print out some data about the table.
    print(table.item_count)

def create_quotation_table():
    db = resource('dynamodb', endpoint_url=endpoint_url)
    table = db.create_table(
        TableName='Quotation',
        KeySchema=[
            {
                'AttributeName': 'quotation_id',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'quotation_timestamp',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'quotation_id',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'quotation_timestamp',
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 100,
            'WriteCapacityUnits': 100
        }
    )

    print("Quotation Table status:", table.table_status)
    # Wait until the table exists.
    table.meta.client.get_waiter('table_exists').wait(TableName='Quotation')

    # Print out some data about the table.
    print(table.item_count)


def my_table_3():
    # db = client('dynamodb', endpoint_url='http://localhost:8000')
    db = resource('dynamodb', endpoint_url='http://localhost:8000')
    #  'batch_get_item', 'batch_write_item', 'create_table', 'get_available_subresources', 'meta', 'tables'
    # print(dir(db))
    # print(db.tables)
    # print(dir(db.tables))
    #  'all', 'filter', 'iterator', 'limit', 'page_size', 'pages'
    # print(db.tables.all()) -> Iterator
    for t in db.tables.all():
        print(t)
    print(dir(t))


#
# create_quotation_item()
# create_item_table()
# create_quotation_table()



def save_to_db(**kwargs):
    print(kwargs)
    print("Data Saved")
    pass


def later_quotation_item():
    db = resource('dynamodb', endpoint_url=endpoint_url)
    table = db.create_table(
        TableName="QuotationItem",
        KeySchema=[
            {
                'AttributeName': '_id',
                'KeyType': 'HASH'
            }],
        AttributeDefinitions=[{'AttributeName': '_id', 'AttributeType': 'S'},
                              {u'AttributeName': u'quotation_id', u'AttributeType': u'S'},
                              {u'AttributeName': u'item_id', u'AttributeType': u'S'},
                              {u'AttributeName': u'quantity', u'AttributeType': u'N'},
                              ],
        GlobalSecondaryIndexes=[
            {
                'IndexName': 'city-index',
                'Projection': {
                    'ProjectionType': 'ALL'
                },
                'ProvisionedThroughput': {
                    'WriteCapacityUnits': index_wcu,
                    'ReadCapacityUnits': index_rcu
                },
                'KeySchema': [
                    {
                        'KeyType': 'HASH',
                        'AttributeName': 'city'
                    }
                ]
            },
            {
                'IndexName': 'name-index',
                'Projection': {
                    'ProjectionType': 'ALL'
                },
                'ProvisionedThroughput': {
                    'WriteCapacityUnits': index_wcu,
                    'ReadCapacityUnits': index_rcu
                },
                'KeySchema': [
                    {
                        'KeyType': 'HASH',
                        'AttributeName': 'name'
                    }]
            },
            {
                'IndexName': 'slug-index',
                'Projection': {
                    'ProjectionType': 'ALL'
                },
                'ProvisionedThroughput': {
                    'WriteCapacityUnits': index_wcu,
                    'ReadCapacityUnits': index_rcu
                },
                'KeySchema': [
                    {
                        'KeyType': 'HASH',
                        'AttributeName': 'slug'
                    }
                ]
            },
            {
                'IndexName': 'email-index',
                'Projection':
                    {
                        'ProjectionType': 'ALL'
                    },
                'ProvisionedThroughput': {
                    'WriteCapacityUnits': index_wcu,
                    'ReadCapacityUnits': index_rcu
                },
                'KeySchema': [
                    {'KeyType': 'HASH',
                     'AttributeName': 'email'
                     }
                ]
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 100,
            'WriteCapacityUnits': 100
        }
    )

    print("Quotation Item Table status:", table.table_status)
    # Wait until the table exists.
    table.meta.client.get_waiter('table_exists').wait(TableName='users')

    # Print out some data about the table.
    print(table.item_count)


def insert_into_table():
    db = resource('dynamodb', endpoint_url=endpoint_url)
    table = 'Item'
    table = db.Table(table)
    print(table.key_schema)
    print(table.item_count)
    table.put_item(
        Item={
            'item_id': 3,
            'item_price': '850',
            'item_name': 'Cookies',
        },
        ConditionExpression=Attr("item_price").ne('850') & Attr("item_id").ne(1)
    )
    print("Row Inserted 1")
    table.put_item(
        Item={
            'item_id': 1,
            'item_price': '901',
            'item_name': 'Pulses',
        },
        ConditionExpression=Attr("item_id").ne(1)
    )
    print("Row Inserted 2")
    response = table.get_item(
        Key={
            'item_id': 1,
            'item_price': '900',
        }
    )
    # print(dir(table))
    # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
    # '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
    # '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
    # '_injector', '_name', 'attribute_definitions', 'batch_writer', 'billing_mode_summary', 'creation_date_time', 'delete',
    # 'delete_item', 'get_available_subresources', 'get_item', 'global_secondary_indexes', 'item_count', 'key_schema',
    # 'latest_stream_arn', 'latest_stream_label', 'load', 'local_secondary_indexes', 'meta', 'name', 'provisioned_throughput', 'put_item',
    # 'query', 'reload', 'restore_summary', 'scan', 'sse_description', 'stream_specification', 'table_arn', 'table_id', 'table_name',
    # 'table_size_bytes', 'table_status', 'update', 'update_item', 'wait_until_exists', 'wait_until_not_exists']

    print(table.item_count)
    print(table.key_schema)
    # response = table.get_item()
    item = response['Item']
    print("Item : ", item)

# create_item_table()
insert_into_table()


############## Ignore Below ################

def get_quotation_1(request):
    if request.method == "POST":
        # Binding data to the form
        form = QuotationForm(request.POST)
        if form.is_valid():
            item_name = form.cleaned_data['item_name']
            quantity = form.cleaned_data['quantity']
            price = form.cleaned_data['price']
            total = form.cleaned_data['total']
            save_to_db(**locals())
            return HttpResponse("Quotation Saved")
            # return HttpResponseRedirect("Quotation Saved")
    else:
        form = QuotationForm()
    context = {'form': form}
    return render(request, 'quotation/home.html', context)

