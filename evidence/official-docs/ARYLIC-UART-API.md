# Arylic UART API — official web documentation

Source: https://developer.arylic.com/uartapi/#uart-api

Imported canonical runtime records: 259–316.

Physical rules: 115200/8/N/1, no flow control, host messages end with semicolon. State messages can be asynchronous.

The source also documents:
- TCP evaluation wrapper `MCU+PAS+RAKOIT:{uart_message}&`
- four-zone RS232 ZON/IDS extension for MA400/HA400/M400/H400
- DEF default-configuration sub-API.

These extensions are documented separately because they are not universally applicable to every A31 product.
