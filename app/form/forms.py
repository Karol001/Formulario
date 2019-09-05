import os 
import re
from django import forms
from app.form.models import Form


Opciones_gente_consciencia = [
       ("1", "Grado de consciencia limitado del propósito o valor del programa Gobierno Datos. "), 
       ("2", "Los ejecutivos son conscientes de la existencia del programa. Hay poco conocimiento del programa fuera de la alta dirección. "), 
       ("3", "Los ejecutivos entienden cómo GD beneficia/impacta su área de la organización, los profesionales del conocimiento son conscientes del programa. Los dirigentes promueven activamente el GD dentro de sus grupos."), 
       ("4", "Los ejecutivos entienden la estrategia de GD a largo plazo y su participación en ella. Los profesionales del conocimiento entienden cómo DG afecta/beneficia a su área de la organización. Los dirigentes activamente promueven DG dentro de sus grupos. "), 
       ("5", "Los ejecutivos entienden la estrategia de GD a largo plazo y su participación en ella. Los profesionales del conocimiento entienden cómo DG afecta/beneficia a su área de la organización. Los dirigentes activamente promueven DG dentro de sus grupos. "), 
       ]

Opciones_politica_consciencia = [
       ("1", "La mayoría de las políticas de los datos existentes están indocumentados y puede haber una comprensión inconsistente de las políticas dentro de un área. "), 
       ("2", "Las directivas existentes se documentan, pero no se mantienen de forma coherente, no están disponibles o no son coherentes entre áreas."), 
       ("3", "Las directivas de datos comunes se documentan y están disponibles a través de un portal común. La mayoría de las partes interesadas son conscientes de la existencia de políticas de datos que pueden afectarlas."), 
       ("4", "Todas las políticas de datos están disponibles a través de un portal común y las partes interesadas reciben una notificación cada vez que se agregan, actualizan o modifican las directivas. "), 
       ("5", "Un historial de todas las políticas de datos se mantiene a través de un portal común y todas las partes interesadas forman parte del proceso de desarrollo de políticas. "), 
       ]

Opciones_capacidades_consciencia = [
       ("1", "Poca conciencia de las capacidades y tecnologías de GD. "), 
       ("2", "Un pequeño subconjunto de la organización comprende las clases generales de las capacidades y tecnologías de GD. "), 
       ("3", "Un pequeño subconjunto de la organización es consciente de las capacidades específicas de GD que están disponibles en la organización. "), 
       ("4", "Se ha identificado un público objetivo y una parte significativa de esa audiencia es consciente de las capacidades de GD que están disponibles en la organización."), 
       ("5", "Una parte significativa del público objetivo entiende cómo utilizar las capacidades de GD que están disponibles en la organización. "), 
       ]

Opciones_gente_formalizacion = [
       ("1", "No hay roles definidos relacionados con GD. "), 
       ("2", "Las funciones y responsabilidades del GD se han definido y examinado con los patrocinadores del programa.  "), 
       ("3", "Algunos roles están disponibles para apoyar las necesidades de GD y los participantes entienden claramente las responsabilidades asociadas con sus funciones. "), 
       ("4", "Los roles GD se organizan en esquemas reutilizables que están diseñados para admitir datos específicos y características funcionales. Hay una amplia (pero incoherente) participación en GD. "), 
       ("5", "Los esquemas organizativos del GD están definidos, se reúnen regularmente y documentan las actividades. "), 
       ]

Opciones_politica_formalizacion = [
       ("1", "No hay políticas formales de GD. "), 
       ("2", "Las políticas de alto nivel de GD están definidas y distribuidas. "), 
       ("3", "Las políticas de datos en torno al gobierno de datos específicos están definidas y distribuidas como mejores prácticas. "), 
       ("4", "Las políticas de datos se convierten en directivas organizacionales y su cumplimiento es auditado. "), 
       ("5", "El cumplimiento de las políticas oficiales de datos de la organización es activamente controlado por un órgano de gobierno. "), 
       ]

Opciones_capacidades_formalizacion = [
       ("1", "Las técnicas y tecnología habilitantes del GD no están definidas. "), 
       ("2", "Están definidas las técnicas y tecnologías habilitantes del GD y se usan soluciones técnicas propias dentro de algunas funciones organizacionales. "), 
       ("3", "Se han adoptado soluciones técnicas propias como mejores prácticas para algunas capacidades del GD y se ponen a disposición en toda la institución. "), 
       ("4", "Todas las capacidades de GD definidas tienen una solución disponible. "), 
       ("5", "Todas las  capacidades de GD definidas son obligatorias para los sistemas asignados o los datos críticos. "), 
       ]

Opciones_gente_metadatos = [
       ("1", "Comprensión limitada de los tipos y el valor de los metadatos. "), 
       ("2", "Los roles responsables de la creación de metadatos técnicos en datos estructurados se definen durante el diseño del sistema. "), 
       ("3", "La responsabilidad de desarrollar definiciones de negocio y almacenarlas en un repositorio central, es asignada y continuamente realizada por expertos en la materia. "), 
       ("4", "Colección de metadatos – validación de responsabilidades son asignadas a individuos específicos para todos los proyectos. "), 
       ("5", "Se crea un grupo de administración de metadatos dedicado para avanzar estratégicamente en las capacidades de metadatos y aprovecharlos de forma más eficaz. "), 
       ]

Opciones_politica_metadatos = [
       ("1", "No hay políticas relacionadas con metadatos. "), 
       ("2", "Se crean y se socializan las mejores prácticas de metadatos. La mayoría de estas se centran en los metadatos asociados con los datos estructurados. "), 
       ("3", "Las políticas que requieren el desarrollo de nuevos metadatos como parte del desarrollo del sistema (normalmente centrados en datos estructurados) se adoptan como políticas oficiales de datos. "), 
       ("4", "Las políticas que requieren la auditoría regular de metadatos en sistemas específicos se adoptan como  políticas de datos oficiales en la organización y el desarrollo de metadatos como parte del desarrollo del sistema se aplica. "), 
       ("5", "La directiva de metadatos cubre los datos estructurados y no estructurados (no tabulares) y se aplica. "), 
       ]

class Opciones_gente_consciencia1(forms.Form):
       class Meta:
              model = Form
              pregunta_gente_conocmiento= forms.CharField (
              label='¿Qué grado de consciencia tienen las personas sobre su papel dentro del programa de gobierno de datos? ', 
              widget=forms.RadioSelect(
                     choices=Opciones_gente_consciencia, 
                     attrs={'class': 'list-unstyled'}))

class Opciones_politica_consciencia1(forms.Form): 
         pregunta_politica_conocmiento= forms.CharField(label='¿Qué conocimiento hay de las políticas, estándares y mejores prácticas de gobernanza de datos?', 
            widget=forms.RadioSelect(
                choices=Opciones_politica_consciencia , 
                attrs={'class': 'list-unstyled'}))

class Opciones_capacidades_consciencia1(forms.Form): 
         pregunta_capacidades_conocmiento= forms.CharField(label='¿Qué grado de consciencia hay en cuanto a las capacidades adquiridas o desarrolladas que habilitan él GD? ', 
            widget=forms.RadioSelect(
                choices=Opciones_capacidades_consciencia , 
                attrs={'class': 'list-unstyled'}))

class Opciones_gente_formalizacion1(forms.Form): 
         pregunta_gente_formalizacion= forms.CharField(label='¿Qué tan desarrollada está la organización de gobierno de datos y qué roles se cumplen para apoyar las actividades de gobierno de datos? ', 
            widget=forms.RadioSelect(
                choices=Opciones_gente_formalizacion , 
                attrs={'class': 'list-unstyled'}))

class Opciones_politica_formalizacion1(forms.Form): 
         pregunta_politica_formalizacion= forms.CharField(label='¿En qué medida se definen, implementan y aplican formalmente las políticas de gobierno de datos? ', 
            widget=forms.RadioSelect(
                choices=Opciones_politica_formalizacion , 
                attrs={'class': 'list-unstyled'}))

class Opciones_capacidades_formalizacion1(forms.Form): 
         pregunta_capacidades_formalizacion= forms.CharField(label='¿Qué tan desarrollado es el conjunto de herramientas que soportan las actividades de gobierno de datos y con qué frecuencia se utiliza ese conjunto de herramientas? ', 
            widget=forms.RadioSelect(
                choices=Opciones_capacidades_formalizacion , 
                attrs={'class': 'list-unstyled'}))

class Opciones_gente_metadatos1(forms.Form): 
         pregunta_gente_metadatos= forms.CharField(label='¿Qué nivel participación hay de las personas de diferentes áreas en el desarrollo y mantenimiento de Metadatos? ', 
            widget=forms.RadioSelect(
                choices=Opciones_gente_metadatos , 
                attrs={'class': 'list-unstyled'}))

class Opciones_politica_metadatos1(forms.Form): 
         pregunta_politica_metadatos= forms.CharField(label='¿En qué medida se definen, implementan y aplican formalmente las políticas de creación y mantenimiento de metadatos?', 
            widget=forms.RadioSelect(
                choices=Opciones_politica_metadatos , 
                attrs={'class': 'list-unstyled'}))

class Opciones_capacidades_metadatos1(forms.Form): 
         pregunta_politica_metadatos= forms.CharField(label='¿En qué medida se definen, implementan y aplican formalmente las políticas de creación y mantenimiento de metadatos?', 
            widget=forms.RadioSelect(
                choices=Opciones_politica_metadatos , 
                attrs={'class': 'list-unstyled'}))

class Formprincipal(forms.ModelForm):
 
 class Meta:
       model= Form

       fields = [
            'Nombre',
            'Cargoform',
            'area',
            'Correo',
        ]

       labels = {

            'Nombre': 'Nombre Completo',
            'Cargoform': 'Cargo',
            'area': 'Area',
            'Correo': 'Correo electrónico',
       }

       widgets = {

            'Nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'Cargoform': forms.TextInput(attrs={'class': 'form-control'}),
            'area': forms.TextInput(attrs={'class': 'form-control'}),
            'Correo': forms.EmailInput(attrs={'class': 'form-control'}),
       }