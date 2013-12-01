Import('env')

if env.TargetPlatform() == 'windows' and ARGUMENTS.get('PRECOMPILED', 'TRUE') != 'FALSE':

    env.Append(CPPDEFINES =['WIN32','CSFUNIFIED_EXPORTS', 'UNIFIED_DLL'])

    env = env.Clone()
    PCH, PCH_OBJ = env.PCH('pre-compiled.cpp')
    env['PCH'] = PCH
    env['PCHSTOP'] = 'pre-compiled.h'
    env.Append(CPPFLAGS=['/FI' + 'pre-compiled.h'])
    # Link the pre-compiled .obj file against every library & program that uses it
    # Otherwise the following warnings are produced
    #    xxx.obj : warning LNK4206: precompiled type information not found;
    #    '..\pre-compiled.obj' not linked or overwritten; linking object as if no debug info
    env.Append(LIBS = [PCH_OBJ])
    Default(PCH)
else:
    import gch2

    gch2.generate(env)

    env['precompiled_header'] = File('/Users/gannons/Development/trunk/tools/pre-compiled/pre-compiled.h')
    env['GchSh'] = env.GchSh(target='/Users/gannons/Development/trunk/tools/pre-compiled/pre-compiled.h.gch', source=env['precompiled_header'])
    env.Append(CPPFLAGS=['-include' + '/Users/gannons/Development/trunk/tools/pre-compiled/pre-compiled.h'])
    #env.gch('pre-compiled.cpp')

    import pdb
    #pdb.set_trace()
