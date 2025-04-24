/**
 * Copyright (c) 2021 Raspberry Pi (Trading) Ltd.
 *
 * SPDX-License-Identifier: BSD-3-Clause
 */

#include <stdio.h>
#include "pico/stdlib.h"
#include "hardware/gpio.h"
#include "hardware/adc.h"
#include "hardware/uart.h"

/* Example code to extract analog values from a microphone using the ADC
   with accompanying Python file to plot these values

   Connections on Raspberry Pi Pico board, other boards may vary.

   GPIO 26/ADC0 (pin 31)-> AOUT or AUD on microphone board
   3.3v (pin 36) -> VCC on microphone board
   GND (pin 38)  -> GND on microphone board
*/

#define ADC_NUM 0
#define ADC_PIN (26 + ADC_NUM)
#define ADC_VREF 3.3
#define ADC_RANGE (1 << 12)
#define ADC_CONVERT (ADC_VREF / (ADC_RANGE - 1))

int main() {
    stdio_init_all();
    sleep_ms(1000);
    printf("Beep boop, listening...\n");

    adc_init();

    // Initialize GPIO pins for ADC0, ADC1, and ADC2
    for (int adc_num = 0; adc_num < 3; adc_num++) {
        adc_gpio_init(26 + adc_num);
    }

    uint adc_raw;
    while (1) {
        for (int adc_num = 0; adc_num < 3; adc_num++) {
            adc_select_input(adc_num); // Select the ADC input
            adc_raw = adc_read();     // Read raw voltage from ADC
            // printf("ADC%d: %.2f V\n", adc_num, adc_raw * ADC_CONVERT);
            printf("ADC%d: %d\n", adc_num, adc_raw);
            // printf("Serial test OK\n");
        }
        sleep_ms(10);
    }
}