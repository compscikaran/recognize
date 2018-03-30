from .models import BlockModel

def last_block():
    return BlockModel.objects.last() 

def next_block(bid):
    for block in BlockModel.objects.all():
        if block.id == bid + 1:
            return block

def verify_chain():
    for block in BlockModel.objects.all():
        if block != BlockModel.objects.last() and block != BlockModel.objects.first():
            nblock = next_block(block.id)
            if block.block_hash != nblock.previous_hash:
                return False
        if block != BlockModel.objects.first():    
            if block.block_hash != block.hash_block():
                return False
    return True

def verify_block_exists(check_block):
    for block in BlockModel.objects.all():
        if block.block_hash == check_block.block_hash:
            return True
    return False





