#ifndef SHA256_H
#define SHA256_H

#include <stdint.h>

void sha256(const void *data, uint64_t len, void *output);

#endif
