
# Class: Parameter


A key/value pair to capture parameter specifications.

URI: [GHGA:Parameter](https://w3id.org/GHGA/Parameter)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ParameterMixin],[AnalysisMethod]++-%20parameters(i)%200..*>[Parameter&#124;parameter_name:string;value:string],[ParameterMixin]++-%20parameters%200..*>[Parameter],[ParameterMixin]++-%20parameters(i)%200..*>[Parameter],[AnalysisMethod]++-%20parameters%200..*>[Parameter],[AnalysisMethod])](https://yuml.me/diagram/nofunky;dir:TB/class/[ParameterMixin],[AnalysisMethod]++-%20parameters(i)%200..*>[Parameter&#124;parameter_name:string;value:string],[ParameterMixin]++-%20parameters%200..*>[Parameter],[ParameterMixin]++-%20parameters(i)%200..*>[Parameter],[AnalysisMethod]++-%20parameters%200..*>[Parameter],[AnalysisMethod])

## Referenced by Class

 *  **[AnalysisMethod](AnalysisMethod.md)** *[AnalysisMethod➞parameters](AnalysisMethod_parameters.md)*  <sub>0..\*</sub>  **[Parameter](Parameter.md)**
 *  **[ParameterMixin](ParameterMixin.md)** *[ParameterMixin➞parameters](ParameterMixin_parameters.md)*  <sub>0..\*</sub>  **[Parameter](Parameter.md)**
 *  **None** *[parameters](parameters.md)*  <sub>0..\*</sub>  **[Parameter](Parameter.md)**

## Attributes


### Own

 * [Parameter➞parameter_name](Parameter_parameter_name.md)  <sub>1..1</sub>
     * Description: The parameter name.
     * Range: [String](types/String.md)
 * [Parameter➞value](Parameter_value.md)  <sub>1..1</sub>
     * Description: The value for an attribute (e.g., a numerical value without the units).
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | SIO:000614 |

