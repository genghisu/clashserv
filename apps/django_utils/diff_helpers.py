import difflib

def generate_diff(original,  final):
    differ = difflib.SequenceMatcher(None,  original,  final)
    result = show_diff(differ)
    return result

def show_diff(seqm):
    """Unify operations between two compared strings seqm is a difflib.SequenceMatcher instance whose a & b are strings"""
    output= []
    for opcode, a0, a1, b0, b1 in seqm.get_opcodes():
        if opcode == 'equal':
            output.append(seqm.a[a0:a1])
        elif opcode == 'insert':
            output.append("<span class='revision_delete'>" + seqm.b[b0:b1] + "</span>")
        elif opcode == 'delete':
            output.append("<span class='revision_add'>" + seqm.a[a0:a1] + "</span>")
        elif opcode == 'replace':
            output.append("<span class='revision_delete'>" + seqm.a[a0:a1] + "</span>")
            output.append("<span class='revision_add'>" + seqm.b[b0:b1] + "</span>")
        else:
            raise RuntimeError, "unexpected opcode"
    return ''.join(output)
