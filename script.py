# -*- coding: utf-8 -*-

names = [
                 ('cnty_cde', 'county_id', lambda x: x),
                 ('sdiv_twp_idn', 'township', lambda x: x),
                 ('sdiv_rng_idn', 'status', lambda x: x),
                 ('elev_df_num', 'df_eleavation', lambda x: x),
                 ('elev_gl_num', 'ground_elevation', lambda x: x),
                 ('elev_kb_num', 'kb_elevation', lambda x: x),
                 ('dpth_tot_num', 'reservoir_total_depth', lambda x: x),
                 ('dpth_tvd_num', 'true_vertical_depth', lambda x: x),
                 ('dpth_mvd_num', 'measured_depth', lambda x: x),
                 ('spud_dte', 'spud_date',
                  lambda x: self._validate_date_xml(x)),
                 ('plug_dte', 'plug_date',
                  lambda x: self._validate_date_xml(x)),
                ]
a = [(x for x in range(10))]
print [x[0] for x in names]