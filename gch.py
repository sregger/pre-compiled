#
# Copyright (C) 2006  Tim Blechmann
# 
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License version 2.1 as published by the Free Software Foundation.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

import SCons.Action
import SCons.Builder
import SCons.Scanner.C

GchAction = SCons.Action.Action('$GCHCOM', '$GCHCOMSTR')

GchBuilder = SCons.Builder.Builder(action = GchAction,
                                   source_scanner = SCons.Scanner.C.CScanner(),
                                   suffix = '$GCHSUFFIX')

def generate(env):
    """
    Add builders and construction variables for the DistTar builder.
    """
    env.Append(BUILDERS = {
        'gch': env.Builder(
        action = GchAction,
        target_factory = env.fs.File,
        ),
        })

    try:
        bld = env['BUILDERS']['Gch']
    except KeyError:
        bld = GchBuilder
        env['BUILDERS']['Gch'] = bld

    env['GCHCOM']     = '$CXX -o $TARGET -x c++-header -c $CXXFLAGS $_CCCOMCOM $SOURCE'
    env['GCHSUFFIX']  = '.gch'


def exists(env):
    return env.Detect('g++')
