
# Class: SoftwareVersion


A key/value pair to capture software version specifications.

URI: [GHGA:SoftwareVersion](https://w3id.org/GHGA/SoftwareVersion)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SoftwareVersionMixin],[AnalysisMethod]++-%20software_versions(i)%200..1>[SoftwareVersion&#124;software:string;version:string],[SoftwareVersionMixin]++-%20software_versions%200..1>[SoftwareVersion],[SoftwareVersionMixin]++-%20software_versions(i)%200..1>[SoftwareVersion],[AnalysisMethod]++-%20software_versions%200..1>[SoftwareVersion],[AnalysisMethod])](https://yuml.me/diagram/nofunky;dir:TB/class/[SoftwareVersionMixin],[AnalysisMethod]++-%20software_versions(i)%200..1>[SoftwareVersion&#124;software:string;version:string],[SoftwareVersionMixin]++-%20software_versions%200..1>[SoftwareVersion],[SoftwareVersionMixin]++-%20software_versions(i)%200..1>[SoftwareVersion],[AnalysisMethod]++-%20software_versions%200..1>[SoftwareVersion],[AnalysisMethod])

## Referenced by Class

 *  **[AnalysisMethod](AnalysisMethod.md)** *[AnalysisMethod➞software_versions](AnalysisMethod_software_versions.md)*  <sub>0..1</sub>  **[SoftwareVersion](SoftwareVersion.md)**
 *  **[SoftwareVersionMixin](SoftwareVersionMixin.md)** *[SoftwareVersionMixin➞software_versions](SoftwareVersionMixin_software_versions.md)*  <sub>0..1</sub>  **[SoftwareVersion](SoftwareVersion.md)**
 *  **None** *[software_versions](software_versions.md)*  <sub>0..1</sub>  **[SoftwareVersion](SoftwareVersion.md)**

## Attributes


### Own

 * [SoftwareVersion➞software](SoftwareVersion_software.md)  <sub>1..1</sub>
     * Description: The software name.
     * Range: [String](types/String.md)
 * [SoftwareVersion➞version](SoftwareVersion_version.md)  <sub>1..1</sub>
     * Description: The software version.
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | SIO:000614 |

