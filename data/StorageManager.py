# import yaml

# !IMPORTANT
# Adding MySQL support but don't have the resources at school

def getStorageProvider():
    return 'JSON'
    # with open('resources/config.yml') as file:
    #     data = yaml.safe_load(file)
    # if data['storage-provider'] == 'JSON' :
    #     return 'JSON'
    # elif data['storage-provider'] == 'MYSQL':
    #     return 'MYSQL'
    # else:
    #     print('Unexpected error while initialising storage provider!')
