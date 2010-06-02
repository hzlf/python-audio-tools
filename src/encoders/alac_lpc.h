#ifndef A_ALAC_ENCODER_LPC
#define A_ALAC_ENCODER_LPC

/********************************************************
 Audio Tools, a module and set of tools for manipulating audio data
 Copyright (C) 2007-2010  Brian Langenberger

 This program is free software; you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation; either version 2 of the License, or
 (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with this program; if not, write to the Free Software
 Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
 *******************************************************/

#include "alac.h"

#define MIN_LPC_ORDER 4
#define MAX_LPC_ORDER 8
#define QLP_COEFFICIENT_PRECISION 16

/*given a set of samples and encoding options,
  returns as a set of LPC coefficients and a shift-needed value*/
void ALACEncoder_compute_best_lpc_coeffs(struct i_array *coeffs,
					 int *shift_needed,

					 int bits_per_sample,
					 struct alac_encoding_options *options,
					 struct i_array *samples);

int ALACEncoder_compute_best_order(struct f_array *error_values,
				   int total_samples,
				   int overhead_bits_per_order);

#endif