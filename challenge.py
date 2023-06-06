features = ['grade',                     # calificación del préstamo

            'sub_grade',                 # subgrado del préstamo

            'short_emp',                 # un año o menos de empleo del prestatario

            'emp_length_num',            # número de años de empleo  del prestatario

            'home_ownership',            # estado de propiedad de vivienda: propio (own), hipoteca (mortgage) o alquiler(rent)

            'dti',                       # relación deuda-ingresos

            'purpose',                   # propósito del préstamo

            'term',                      # plazo del préstamo

            'last_delinq_none',          # ¿el prestatario ha tenido algún impago?

            'last_major_derog_none',     # ¿el prestatario ha tenido una calificación de 90 días o peor?

            'revol_util',                # porcentaje de crédito disponible utilizado

            'total_rec_late_fee',        # total de cargos por pagos atrasados recibidos hasta la fecha

            ]




target = 'bad_loans'                    # prediction target (y) (+1 significa seguro, 0 is arriesgada)




# Extraemos feaures y variable safe_loans

data = data[features + [target]]