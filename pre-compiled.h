#define CERT_CHAIN_PARA_HAS_EXTRA_FIELDS // required to use dwUrlRetrievalTimeout in CERT_CHAIN_PARA

#if defined(WIN32)
#include <winsock2.h>
#include <windows.h>
#include <windef.h>
#endif
#include <vector>
#include <map>
#include <iostream>
#include <fstream>
#include <string>