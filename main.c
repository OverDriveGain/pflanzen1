#include <stdio.h>
#include <string.h>

#include <msg.h>
#include <shell.h>

#include "lib/network.c"
#include "lib/pump.c"
#include "lib/sensor.c"
#include "lib/util.c"

#define MAIN_QUEUE_SIZE     (8)
static msg_t _main_msg_queue[MAIN_QUEUE_SIZE];

static const shell_command_t shell_commands[] = {
    { "light", "read light data", read_light },
    { "humidity", "read humidity data", read_humidity },
    { "udp_dumpd", "start debug udp server that just prints data it receives", dump_server },
    { NULL, NULL, NULL },
};

int main(void)
{
    msg_init_queue(_main_msg_queue, MAIN_QUEUE_SIZE);
    printf("[Pflanzen 1] Welcome! I am a %s.\n", NODE_ROLE);

    char line_buf[SHELL_DEFAULT_BUFSIZE];
    shell_run(shell_commands, line_buf, SHELL_DEFAULT_BUFSIZE);

    return 0;
}
