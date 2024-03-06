
def textBlockWidth(block):
    return len(max(block.split('\n'), key=lambda x: len(x)))


def textBlockHeight(block):
    return block.count('\n') + 1