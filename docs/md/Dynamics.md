# EMT Dynamics {#target-dynamics}

The package uses *DetailedModelTypeDynamics* to support the standard
library models in the *Emtiop* profile. To add more model types, edit
*detailed_model_types.json* in the *queries* subdirectory of the package
source. The CIM *StandardModels* for controllers are not supported in
*Emtiop*; only the *SynchronousMachineTimeConstantReactance* is used
from *StandardModels*.

For each dynamics controller type supported, the following attributes
are defined on the CIM class *NthAmDynamicModel*:

-   **Model (Header)**: a mnemonic for this controller type, typically a
    6-character codeword from the original *dyr* file schema.
-   **nameKind**: the domain from which the *Model* name comes. May be
    *AUX*, *DGS*, *DYD*, *DYR* or *Other*. Use *Other* for user-code
    models that are not implemented in a DLL.
-   **modelKind**: the expected application of this controller type. The
    package currently supports *machine*, *renewableEnergyResource*,
    *excitationSystem*, *powerSystemStabilizer*, and *turbineGovernor*.
-   **statusKind**: the allowable use of this controller type for
    interconnection-wide studies in North America. May be *allowed*,
    *deprecated*, or *prohibited*.
-   **description**: brief description of the controller, if available.
    Otherwise, use *Model* and *modelKind* for interpretation.
-   **closestStandardModel**: the name of the best-matching model from
    *StandardModels* in the CIM *Dynamics* package. There may not be a
    close match. If there is a match, it may provide default values and
    units from the CIM documentation.
-   **mRID**: a unique CIM identifier for this controller type,
    maintained within this package.

Each supported dynamics controller type has a list of parameters. These
map to the CIM class *ParameterDescriptor*.

-   **name**: the name of the parameter, from orginal *dyr* file format
-   **mRID**: a unique CIM identifier for this parameter descriptor,
    maintained within this package.
-   **(sequence)Number**: an integer sequence number from original *dyr*
    file format. The sequence numbers of interest usually begins with
    **3**, because first three *dyr* parameters (*Bus*, *Model*, *ID*)
    are not handled as CIM model parameters.
-   **(typical)Value**: a default value, if available from a matching
    CIM attribute in the *closestStandardModel* class.
-   **(engineering)Unit**: the expected input units, if available from a
    matching CIM attribute in the *closestStandardModel* class.

For EMT netlisting, use the CIM RDF queries *EMTDynamicsModel*,
*EMTDynamicsModelType*, *EMTDynamicsModelParameterDescriptor* and
*EMTDynamicsParameter* to retrieve the data. Refer to the original *dyr*
format documentation to interpret the applications, parameter names and
signal connections for each model type.

## AUX Files

## DGS Files

## DYD Files

## DYR Files

### EXST1

**nameKind**: DYR

**modelKind**: excitationSystem

**statusKind**: allowed

**description**:

**closestStandardModel**: ExcST1A

**mRID**: C8DA2CB6-6699-4EE7-9AE6-FE0FE22DB229

  --------------------------------------------------------------------------------------------------
  Name           Number         Value          Unit           mRID
  -------------- -------------- -------------- -------------- --------------------------------------
  Bus            1                             Integer        64D9432B-5466-4201-BC3E-6644F8F2EB75

  Model          2                             String         679E5D3B-6D51-44F9-B659-2F0D2024D8F7

  ID             3              1              String         93720EDE-2C55-4055-B700-9897AE0BF544

  TR             4                                            CB71678F-2489-4392-A902-2829A8BF7A79

  VIMAX          5              0.1            PU             79326BD2-E93E-43A5-978C-67FD273BF4B7

  VIMIN          6              -0.1           PU             248B970E-A434-416A-B70E-574B18238F12

  TC             7              1.0            Seconds        5DCA73CD-94F6-43F2-8A6C-3536A37AC895

  TB             8              10.0           Seconds        953919DC-E8B4-46FA-A3F9-532B8088440E

  KA             9              40.0           PU             F44C075A-280A-4B13-8D6A-4FD378F90D62

  TA             10             0.0            Seconds        1299F2CC-34FE-4FE3-9446-C8C8F7BCECBA

  VRMAX          11             4.5            PU             069F89A9-DA85-49EC-869A-A08926CF0BFD

  VRMIN          12             -4.0           PU             AD2D1F99-BFDB-4D25-B887-232AE715B38C

  KC             13             0.038          PU             1160B75E-445F-4DEB-A6C9-A0A5F255FD10

  KF             14             0.0            PU             502534AF-9A0C-4C4E-82A1-EE7DC5008296

  TF             15             1.0            Seconds        095932C8-2280-4B7A-BBBE-A4F1328EB5DE
  --------------------------------------------------------------------------------------------------

  : EXST1 Parameters

### GAST

**nameKind**: DYR

**modelKind**: turbineGovernor

**statusKind**: prohibited

**description**:

**closestStandardModel**: GovGAST

**mRID**: 29FF9352-92BE-4FFD-997A-749ADC634210

  --------------------------------------------------------------------------------------------------
  Name           Number         Value          Unit           mRID
  -------------- -------------- -------------- -------------- --------------------------------------
  Bus            1                             Integer        6A42DEEC-D642-4609-A960-58F3986FB50E

  Model          2                             String         B87C6967-BC0C-4103-9D12-FEA161036F1D

  ID             3              1              String         CC395F87-C6C5-43AF-9285-7755602FFD99

  R              4              0.04           PU             CB95A3BF-352B-418B-B0C9-475BE1358A19

  T1             5              0.5            Seconds        CD6015AA-7290-4EAC-9170-74E6854AEABA

  T2             6              0.5            Seconds        66C2A1AE-A75E-47DE-B28A-89DB41CFC9B2

  T3             7              3.0            Seconds        9531379C-9987-448B-93F2-C93367255C10

  AT             8              1.0            PU             B16EC670-A401-410E-A063-F52BF42C666D

  KT             9              3.0            PU             2613C99B-D811-4C55-9576-199FD4A6560E

  VMAX           10             1.0            PU             9CD50017-DCF2-4A34-990E-71775206495B

  VMIN           11             0.0            PU             A89155CF-28AE-49FA-845C-BEFB840D366B

  Dt             12             0.18           PU             CCC1AE88-3059-4ED4-BFE7-73862D183C07
  --------------------------------------------------------------------------------------------------

  : GAST Parameters

### GENCLS

**nameKind**: DYR

**modelKind**: machine

**statusKind**: prohibited

**description**:

**closestStandardModel**: SynchronousMachineSimplified

**mRID**: 5CD518B0-8D8A-4020-AEB0-B41EC186DDC3

  --------------------------------------------------------------------------------------------------
  Name           Number         Value          Unit           mRID
  -------------- -------------- -------------- -------------- --------------------------------------
  Bus            1                             Integer        BC3AEB61-662E-47AA-8956-68D93978BDFF

  Model          2                             String         2A681790-3ABC-4697-BB4C-8C6F7F80751A

  ID             3              1              String         8D738EAB-9017-4E0F-91FE-45B063ABFBC7

  H              4              3.0            Seconds        AD0CFE37-D644-4FD2-9B3A-81C6028527B0

  D              5              0.0            Float          DDAF1A07-94BB-4F66-B03B-D0C988D6B68E
  --------------------------------------------------------------------------------------------------

  : GENCLS Parameters

### GENROU

**nameKind**: DYR

**modelKind**: machine

**statusKind**: deprecated

**description**:

**closestStandardModel**: SynchronousMachineTimeConstantReactance

**mRID**: EE35876D-BB35-4573-B16B-DC3A66702322

  --------------------------------------------------------------------------------------------------
  Name           Number         Value          Unit           mRID
  -------------- -------------- -------------- -------------- --------------------------------------
  Bus            1                             Integer        DF6465B4-FC2E-4515-9C1F-44DEEB8AA28F

  Model          2                             String         DC35B3CA-4B12-4A94-B592-E7BE86CFCC90

  ID             3              1              String         5188FD9C-BA21-47E3-BBEB-76CC38C0CB10

  Td10           4              7.563          Seconds        25032EC4-FA15-4C83-860E-32D8EB13D88C

  Td20           5              0.017          Seconds        149D6972-5E43-4E41-A0A5-F54B89E267F4

  Tq10           6              1.133          Seconds        1D5F030D-F946-45F1-9F8E-16EC8BB54F0E

  Tq20           7              0.05           Seconds        2C60A143-5190-420E-BE5E-56F00522F3F3

  H              8              3.0            Seconds        426AA788-6D71-4E75-8124-BA345F32D5F5

  D              9              0.0            Float          08D55B1A-A8E2-400B-8E3D-EA1AFEF27C46

  Xd             10             1.43           PU             D3B8A25D-E4B9-4435-A46A-7615939424ED

  Xq             11             1.33           PU             F83388F7-6B84-4893-9326-0A81043D40F3

  Xd1            12             0.146          PU             98CE0D22-1F07-46CA-BBB4-8E8049FC90DF

  Xq1            13             0.258          PU             E1D7AE94-C0EC-4D93-A14E-C12770D2C77F

  Xd2            14             0.114          PU             7D910E14-5835-44AA-857A-907A3F97F918

  Xl             15             0.096          PU             40F8F789-EEFB-4259-B50E-E6B806899343

  S10            16             0.02           Float          FCB1A458-A938-4467-98D9-4096737FE78D

  S12            17             0.12           Float          A7BA2517-3D89-4026-A90B-E8FE1A68F24E
  --------------------------------------------------------------------------------------------------

  : GENROU Parameters

### GENSAL

**nameKind**: DYR

**modelKind**: machine

**statusKind**: prohibited

**description**:

**closestStandardModel**: SynchronousMachineTimeConstantReactance

**mRID**: F44A9DA5-A1F6-41C7-BD55-48A744850B3D

  --------------------------------------------------------------------------------------------------
  Name           Number         Value          Unit           mRID
  -------------- -------------- -------------- -------------- --------------------------------------
  Bus            1                             Integer        4D9BD4E8-A771-4C65-9BB5-3D786F0C5B3A

  Model          2                             String         B22DC44E-B45B-4832-B70D-6EA69AEBCDDE

  ID             3              1              String         23A908A0-1931-464F-AEEB-2CE328F20B61

  Td10           4              7.563          Seconds        78CCB41D-D801-45C2-B6FC-C89209083A3F

  Td20           5                                            063E48CE-988F-453D-97A0-7BC8C734BD58

  Tq20           6                                            E3863138-5E6D-4C86-87A2-13BE6F4E624C

  H              7              3.0            Seconds        010FBF35-A869-40BA-8D04-5F9F36B335AA

  D              8              0.0            Float          6FE8A59B-400B-468E-906C-ED74BFF7E6A6

  Xd             9              1.43           PU             C693B998-673E-4CC4-8B51-57A4268D2209

  Xq             10             1.33           PU             BE1A1169-154C-4FAC-93B5-6D9BF25AB8B7

  Xd1            11             0.146          PU             7E5C18A5-7272-4533-AAB5-E524364DC249

  Xd2            12             0.114          PU             34A9A563-A55C-4F8B-8C8F-18298AB8EB47

  Xl             13             0.096          PU             B771A5AA-44D6-4092-920E-3494DE3E626F

  S10            14             0.02           Float          087C10FD-75B9-4435-AE76-3177159FCC91

  S12            15             0.12           Float          57600D39-5AA3-4BD4-B457-C3BD1B80AC60
  --------------------------------------------------------------------------------------------------

  : GENSAL Parameters

### HYGOV

**nameKind**: DYR

**modelKind**: turbineGovernor

**statusKind**: allowed

**description**:

**closestStandardModel**: GovHydro1

**mRID**: 7C2D15AE-D394-44A7-96CB-5C80427A42B6

  --------------------------------------------------------------------------------------------------
  Name           Number         Value          Unit           mRID
  -------------- -------------- -------------- -------------- --------------------------------------
  Bus            1                             Integer        01C9398B-A526-4BE2-A369-F0934BE09D86

  Model          2                             String         EEBC03F2-B78A-4A2E-B777-31DFCE7A0D53

  ID             3              1              String         C1AC96C6-2E6C-4883-A312-24013C56FF48

  R              4              0.04           PU             6880E7DA-6B48-44CC-945F-BDEAB96CA696

  r              5              0.3            PU             41FF412D-FECF-44D4-B6B2-EF1AF70532C2

  Tr             6              5.0            Seconds        6355ED50-353B-47C4-86CA-AFAB3ABAEBDB

  Tf             7              0.05           Seconds        FC365731-77BE-406B-804D-AC8E4A4C4D3E

  Tg             8              0.5            Seconds        D253096C-0E85-47E9-B471-1DCA2EFF263D

  VELM           9              0.2            Float          3C592791-CE83-417D-9F38-899FE3310908

  GMAX           10             1.0            PU             5CD6DA0E-369D-4BDC-8DEB-8CAD4E6D000A

  GMIN           11             0.0            PU             1F710253-5741-454E-95BC-3AEB3208D8ED

  Tw             12             1.0            Seconds        066BB9BC-2E8B-4C80-816E-E53964C377BF

  At             13             1.2            PU             FDC81E4B-12CA-46A3-B354-4E7CD90223B4

  Dturb          14             0.5            PU             04804D4B-E401-453C-BD94-67B940740AB7

  qNL            15             0.08           PU             8DE593E0-BFCB-45B8-ADC2-EF85B981FE26
  --------------------------------------------------------------------------------------------------

  : HYGOV Parameters

### IEEEST

**nameKind**: DYR

**modelKind**: powerSystemStabilizer

**statusKind**: allowed

**description**:

**closestStandardModel**: Pss1A

**mRID**: 88DA0C9F-1A84-46A4-B8AC-1DD293730816

  -----------------------------------------------------------------------------------------------------------------------
  Name           Number         Value                            Unit              mRID
  -------------- -------------- -------------------------------- ----------------- --------------------------------------
  Bus            1                                               Integer           8D35215A-1544-46BB-8310-3AB2023AADF8

  Model          2                                               String            CABE4911-0CF3-4A50-8039-44ADFA9D38B9

  ID             3              1                                String            13B5AEB6-0D8A-4B07-A5A9-D6F481D85DF1

  MODE           4              rotorAngularFrequencyDeviation   InputSignalKind   4E329B38-269A-4906-98C9-B8D6D87F4CE3

  BUSR           5                                                                 AE1A189E-90DC-4820-A0B6-DCF485F1FA86

  A1             6              0.0                              PU                3C687FA6-309A-4DEC-B945-D616E00C4165

  A2             7              0.0                              PU                2D1BD53F-A65E-448D-8186-0EFDE2C60CAC

  A3             8              0.0                              PU                010E719E-9B1A-4991-A47D-DF67285F475F

  A4             9              0.0                              PU                A5380CA1-5782-4EB6-9352-83835BF36273

  A5             10             0.0                              PU                7E941B65-70F9-4E23-8257-2C5E8776E28D

  A6             11             0.0                              PU                8D4541DA-F458-48A0-B00A-C0B628E93E08

  T1             12             1.0                              Seconds           1B4B54DC-C4C9-458A-8EDE-535C077F1156

  T2             13             0.5                              Seconds           343361F9-5599-4CA6-A451-9B2A601E4393

  T3             14             2.0                              Seconds           2EC855E9-0CB9-4C4D-99C8-2743C28AB462

  T4             15             0.1                              Seconds           F06FC26A-B4F6-4760-9AD3-A934A0C13C0B

  T5             16             10.0                             Seconds           7D7B8E7B-A548-4623-A117-D0677B6BF6C3

  T6             17             0.0                              Seconds           7FF23EEA-6198-41CD-8725-3DB9030BABAC

  KS             18             2.0                              PU                C89902D5-EE8A-4D09-859B-998E19FEA3A4

  LSMAX          19                                                                95E86A1A-54D0-4C70-8050-6084849A527A

  LSMIN          20                                                                795EB7B3-1BFC-4831-8E07-7A23026F42BB

  VCU            21             5.0                              PU                24FE04AC-5723-41AF-858D-7884A0FC5E71

  VCL            22             -5.0                             PU                D91DACFF-9614-4967-8012-50DE0A3474D6
  -----------------------------------------------------------------------------------------------------------------------

  : IEEEST Parameters

### IEEET1

**nameKind**: DYR

**modelKind**: excitationSystem

**statusKind**: allowed

**description**:

**closestStandardModel**: ExcIEEEDC1A

**mRID**: 1D697002-8710-4710-9717-6B074A9F66EF

  --------------------------------------------------------------------------------------------------
  Name           Number         Value          Unit           mRID
  -------------- -------------- -------------- -------------- --------------------------------------
  Bus            1                             Integer        A2D8BF5B-322A-4AB0-925D-F172700930A7

  Model          2                             String         ED1B2A45-0F14-421D-B913-F281302F101D

  ID             3              1              String         0FD64F33-C52A-47EB-90FC-051C9B6FDB23

  TR             4                                            90392B45-2438-4859-BA0C-274940B62CE4

  KA             5              46.0           PU             06D9C5F6-2AE2-4B19-9CF3-51F7524E04E5

  TA             6              0.06           Seconds        6E3516C8-8BA3-4F0C-A793-7893E0A054D0

  VRMAX          7              1.0            PU             FD880F5C-AD4A-47AB-A26B-5124AA6902A3

  VRMIN          8              -0.9           PU             DBB46C29-E4C4-4CD2-BB5C-0D2C838C89BA

  KE             9              0.0            PU             BF4C1769-0357-49BE-8627-7B9CD0D90F60

  TE             10             0.46           Seconds        6D737FCB-269D-4868-9E98-D1AA7F43C3B3

  KF             11             0.1            PU             988B4A18-B5A6-47AE-91D3-68D5DD6290E8

  TF             12             1.0            Seconds        EAB5AEC3-DE88-4016-B97F-66D9CDA67611

  Switch         13                                           7E7F6414-7AEF-4C23-9C43-82F28D949F3B

  E1             14             3.1            PU             C9479F9A-722D-416D-8D8E-71FAD92390A9

  SE1            15             0.33           Float          9A40656D-D77E-46B0-B706-7797A5F290D5

  E2             16             2.3            PU             A8A65F06-88C2-4203-ACD8-41BDD15A966F

  SE2            17             0.1            Float          E461B486-F24C-4BDD-93A7-CF07A9B971E3
  --------------------------------------------------------------------------------------------------

  : IEEET1 Parameters

### IEESGO

**nameKind**: DYR

**modelKind**: turbineGovernor

**statusKind**: prohibited

**description**:

**closestStandardModel**: GovSteamSGO

**mRID**: F825AD7A-F24D-485E-9347-D437A4714031

  --------------------------------------------------------------------------------------------------
  Name           Number         Value          Unit           mRID
  -------------- -------------- -------------- -------------- --------------------------------------
  Bus            1                             Integer        48689ECA-7FB8-469B-A7BD-7FD2CF437EC7

  Model          2                             String         97A784C4-F9C3-4F2B-A2D4-C28B3581F6C4

  ID             3              1              String         35504746-086F-4918-8C9F-AB270E4F06CF

  T1             4              5.0            Seconds        F92CC7D1-E58E-4C96-B5F5-FF18FB934D71

  T2             5              5.0            Seconds        D935A410-9662-4811-BB7B-81B0907895CB

  T3             6              0.1            Seconds        CAF5FFF9-ECBE-4A8B-A391-7568DB44B078

  T4             7              0.0            Seconds        39E52BDC-255A-49B2-BE80-92E20240C63E

  T5             8              0.0            Seconds        18E1330D-02DD-4C0E-9E9A-FA406AEFEE76

  T6             9              0.0            Seconds        1C2B1AC1-177A-4EAB-9322-D6DEF1B995D8

  K1             10             25.0           PU             666A1142-4B6E-4942-984E-24FF97A5A62D

  K2             11             0.0            PU             259A5850-9DEF-47B0-A34A-8D1F4876210C

  K3             12             0.0            PU             2C884552-0A10-4E68-8302-19695662A563

  PMAX           13             0.9            PU             4FB81493-5BD7-4AC1-BC71-90E7C6BE008D

  PMIN           14             0.05           PU             F4F40632-4BA4-47C6-B3A4-D9ECBADD6593
  --------------------------------------------------------------------------------------------------

  : IEESGO Parameters

### REECA1

**nameKind**: DYR

**modelKind**: renewableEnergyResource

**statusKind**: allowed

**description**:

**closestStandardModel**: WeccREECA

**mRID**: 737C9425-B23D-4692-BB9D-6C1801A341BE

  --------------------------------------------------------------------------------------------------
  Name           Number         Value          Unit           mRID
  -------------- -------------- -------------- -------------- --------------------------------------
  Bus            1                             Integer        2FAEA6F3-3016-4491-BDA0-103200BA5747

  Model          2                             String         E0886164-F8BC-422D-A29D-16201DE9AA77

  ID             3              1              String         4E39C110-9848-49BC-876E-14ED740C4093

  BUSR           4                                            1CA731D1-E8F8-42DB-8E58-DA4B9B4DF9A9

  PFFLAG         5              False          Boolean        AF0BF4AF-764A-4628-AAB8-19225B40A158

  VFLAG          6              True           Boolean        ACEA907F-0EF7-477C-81D9-7CC34BC16131

  QFLAG          7              True           Boolean        786A2C31-C177-448E-86CA-7E56F04ADB41

  PFLAG          8              True           Boolean        03067421-28C4-4AF8-B5BC-F4F0ED7B6020

  PQFLAG         9              False          Boolean        BDF4DE52-2DBE-46FD-853E-1773C2327B6B

  Vdip           10             0.87           PU             2F0F6B77-D760-4F6C-8D1B-392A3585FD42

  Vup            11             1.15           PU             A8A79AB1-06D8-4EB5-8789-804DB75C179C

  Trv            12             0.03           Seconds        6D2B92F8-30CD-4D7E-9169-C9A28224F03B

  dbd1           13             -0.05          PU             81A62F12-5154-48FB-8E58-C092D556B9CD

  dbd2           14             0.05           PU             376022E5-AFA5-40C1-96D9-E4F70F848656

  Kqv            15             5.0            PU             9335B9A4-747B-437A-99F4-204967E17E6F

  Iqh1           16             1.05           PU             C63ADBF4-919D-4787-BD71-34B568D41C8C

  Iql1           17             -1.05          PU             7E2A4B97-8ABF-43CF-9D7D-81334EA8DB7F

  Vref0          18             1.0            PU             BBB70981-1913-45EA-A8C0-4E7B935CDF21

  Iqfrz          19             0.05           PU             9C3747D1-F1CA-419E-9564-77912CF01ACE

  Thld           20             0.0            Seconds        5CBA6640-2682-4FD7-BF12-1A8B906497D8

  Thld2          21             0.0            Seconds        49E007D9-1474-40AC-A5F9-C091BCD70704

  Tp             22             0.05           Seconds        92C925AE-4C42-421A-9ADE-0BEB3E6B3D85

  QMax           23             0.7            PU             2BCC9F74-3065-4293-B7D9-6656FD97FD26

  QMin           24             -0.7           PU             B60E708D-BFAF-4BCC-BFB6-B93E722E2616

  VMAX           25             1.07           PU             2A95B34F-025C-4ACD-AABD-C51E487ED44A

  VMIN           26             0.9            PU             8BC2AA90-AF1A-40AC-9794-98EEDDA69B8C

  Kqp            27             0.1            PU             ED37BC37-3EA1-4DA1-819A-5A4A426DD864

  Kqi            28             0.1            PU             A6CDABC0-69EB-4141-B5F8-360AD976FCF5

  Kvp            29             5.0            PU             62F16062-1BF3-49FD-B2F4-7CE208A297FB

  Kvi            30             1.0            PU             346F4B13-FD65-4E57-868F-AFC2DC3966F5

  Vbias          31             0.0            PU             C1CBD55E-8049-4DBB-8AC8-6556AFAD243F

  Tiq            32             0.015          Seconds        037C243D-5476-4FA4-903F-3DE832AB97CE

  dPmax          33             999.0          PU             9FEFADB8-FCA6-467E-A0E0-6A0B8070418C

  dPmin          34             -999.0         PU             370643E2-4DA4-42FB-A876-5FCBE065B5B7

  PMAX           35             1.0            PU             19F78225-C18F-4719-8D24-EED695C07960

  PMIN           36             0.0            PU             C6AC5C89-7A2F-4437-BAA9-BC8D0FEA4730

  Imax           37             1.2            PU             1395498F-FE58-4DEE-B0AD-B6C1819E4990

  Tpord          38             0.03           Seconds        BF07A12F-1BA1-4D3D-A577-52F398259E19

  Vq1            39             -1.0           PU             143CC459-8716-4B19-A68F-251F8FE10BF9

  Iq1            40             1.0            PU             6994AC3F-5173-454C-8778-D96D0444276B

  Vq2            41             2.0            PU             E23B8641-EF32-4D48-A58C-CEC86DB07934

  Iq2            42             1.0            PU             D241E5C1-F4DB-4654-B9A3-3EB7D40667EE

  Vq3            43             0.0            PU             B254F02C-781F-4547-8E08-25604E82D04D

  Iq3            44             0.0            PU             B9B701FD-166D-41BB-9647-4547B48564F4

  Vq4            45             0.0            PU             712D3456-5E20-4D6C-9C73-67AC138CA33D

  Iq4            46             0.0            PU             3CF71436-E804-4378-ABB7-B3F22497BADC

  Vp1            47             -1.0           PU             B4556CE5-5583-424D-B0F1-1F82C056803F

  Ip1            48             1.0            PU             352229D4-CFB4-4F23-B8C2-D36A5C7D401D

  Vp2            49             2.0            PU             31832411-11CC-4FDE-8D39-3F03A8411A3F

  Ip2            50             1.0            PU             319A0D2C-2719-4CB6-94AD-04386C646CDD

  Vp3            51             0.0            PU             4AF992A7-010D-42CF-890B-DA4A92212AB1

  Ip3            52             0.0            PU             10947A42-96E4-46D4-9524-3734F3FC497B

  Vp4            53             0.0            PU             FB0B16CC-534F-41FF-87A6-2B76CC033CAF

  Ip4            54             0.0            PU             2AAD6538-D75E-4AFF-BE8A-DAF56935C8CE
  --------------------------------------------------------------------------------------------------

  : REECA1 Parameters

### REECB1

**nameKind**: DYR

**modelKind**: renewableEnergyResource

**statusKind**: prohibited

**description**:

**closestStandardModel**: WeccREECA

**mRID**: B4680043-B42B-4ABF-8875-E7A281A3D5B8

  --------------------------------------------------------------------------------------------------
  Name           Number         Value          Unit           mRID
  -------------- -------------- -------------- -------------- --------------------------------------
  Bus            1                             Integer        59AB3E8E-F13E-48E8-B4C1-5958E9B854C5

  Model          2                             String         C546FD6B-D2FA-4977-9FA0-52290697D27B

  ID             3              1              String         0B13A538-7510-4BD8-9AF7-39BCDCF6B66C

  PFFLAG         4              False          Boolean        767B6CDB-5513-4704-841E-59AA0C758472

  VFLAG          5              True           Boolean        A4ABD856-A607-44E3-92B8-B02F60BFF739

  QFLAG          6              True           Boolean        E64D8020-5AF7-4FFA-8DEE-7F45CC0186A4

  PFLAG          7              True           Boolean        298A347A-1FB9-40C0-ADDF-FAB7566B8145

  PQFLAG         8              False          Boolean        CA39CA54-19E5-4F08-8633-03C14B8BF029

  Vdip           9              0.87           PU             1576C754-2DE1-4D1A-A318-0B0F8A2BF76A

  Vup            10             1.15           PU             E91890F2-5A16-431D-B4E5-63B4B2E7EEB9

  Trv            11             0.03           Seconds        8CB649B1-E009-45EC-92D2-3B0A83A7F411

  dbd1           12             -0.05          PU             BE92D39B-6DCF-499A-B9C8-DC04BF1F4566

  dbd2           13             0.05           PU             BC9F8A06-F60B-482C-8FAB-DEDA9F288CC6

  Kqv            14             5.0            PU             42483453-93FE-4710-9D07-841BFC6CAA22

  Iqh1           15             1.05           PU             E18946BC-DE03-42DB-B89E-035B1FF797D7

  Iql1           16             -1.05          PU             E1BDF520-638A-484B-86D3-5C54EEE6B636

  Vref0          17             1.0            PU             86006D8F-A043-43F5-A7EF-DD537A6124A5

  Tp             18             0.05           Seconds        A95F6111-9CDC-40A2-8750-6A9DD31E3BD8

  QMax           19             0.7            PU             A33C4B03-9188-4BA4-8CD5-65622596F469

  QMin           20             -0.7           PU             B722E85B-287A-49E3-BC78-A15314F2BA40

  VMAX           21             1.07           PU             E893FCED-668A-4917-9457-51FE38B5A314

  VMIN           22             0.9            PU             A3114F1D-5BEA-4716-BFE6-1E283371FE3D

  Kqp            23             0.1            PU             9CB6F2A3-435E-44E9-81B5-0CB0F339F881

  Kqi            24             0.1            PU             4D20D1F6-159C-4559-A148-63A82944160A

  Kvp            25             5.0            PU             A68174BA-EB89-41AE-9E73-B72CF37BE72F

  Kvi            26             1.0            PU             A38C1CF1-B6CB-4C58-A3E2-1E865DFCB359

  Tiq            27             0.015          Seconds        1A13F00E-4101-42A1-ADA6-069D113D3C34

  dPmax          28             999.0          PU             56D7E6FE-035D-4524-B071-F4CD0EF2204C

  dPmin          29             -999.0         PU             6BFD4D02-64C3-4B59-A00F-6B3CD9FD3D61

  PMAX           30             1.0            PU             1C9E0D6E-0F44-462A-B632-954A6E9C784E

  PMIN           31             0.0            PU             3625354D-03D0-47E7-95C9-EF89512F9506

  Imax           32             1.2            PU             1E9969CE-BDB4-4F08-AC0D-25F96034233B

  Tpord          33             0.03           Seconds        AA624219-4CB6-4377-BE2D-64504D41D666
  --------------------------------------------------------------------------------------------------

  : REECB1 Parameters

### REGCA1

**nameKind**: DYR

**modelKind**: renewableEnergyResource

**statusKind**: allowed

**description**:

**closestStandardModel**: WeccREGCA

**mRID**: ED023EB7-2094-44E5-94E1-A6A4BDDC9BA8

  --------------------------------------------------------------------------------------------------
  Name           Number         Value          Unit           mRID
  -------------- -------------- -------------- -------------- --------------------------------------
  Bus            1                             Integer        DB3B77A0-8CF1-499C-9E27-555B4F7E53BB

  Model          2                             String         D3329ED5-3D8A-482F-BFC4-BB87CC921725

  ID             3              1              String         CD5A7A89-E411-4CB3-B864-CD7BBDFA788A

  Lvplsw         4              True           Boolean        83AB5D99-8196-4243-A3AA-B07B201C4326

  Tg             5              0.02           Seconds        D6980FD5-7C98-4CCA-877A-62933645447B

  Rrpwr          6              10.0           PU             1BD3442D-C02B-4F7C-B622-4E30A1E2CEB4

  Brkpt          7              0.9            PU             5A737BB4-EEA3-486E-8CC8-539E68A8535C

  Zerox          8              0.4            PU             A8914BCC-F7DD-4D17-9E31-653DF9574126

  Lvpl1          9              1.2            Float          1C552845-EFF1-41FE-8675-13942D1998EF

  Volim          10             1.2            PU             DD4D6806-5715-4CC6-9BA4-533808562B15

  Lvpnt1         11             0.8            PU             2851E921-7603-4FEF-905B-DA437652F5B6

  Lvpnt0         12             0.4            PU             42881242-0903-44F8-A565-A9273B186223

  Iolim          13             -1.2           PU             37B6A0A0-E321-4310-8628-2DE1A38049CB

  Tfltr          14             0.015          Seconds        A1B04507-70C4-47FC-8BDC-7BA27ABC1004

  Khv            15             0.7            Float          CA6613C5-B2D6-4792-87DB-D070DBB135D8

  Iqrmax         16             999.0          PU             93487D57-F243-425B-ACA0-D46A78117183

  Iqrmin         17             -999.0         PU             237103F2-35B0-4DB3-AAF3-1906C3C5AC8A

  Accel          18                                           7058A063-4FEC-4A0B-A459-19BC3F4C4445
  --------------------------------------------------------------------------------------------------

  : REGCA1 Parameters

### REPCA1

**nameKind**: DYR

**modelKind**: renewableEnergyResource

**statusKind**: allowed

**description**:

**closestStandardModel**: WeccREPCA

**mRID**: 32034FA3-7303-4F91-8110-A05EE463DF7F

  --------------------------------------------------------------------------------------------------
  Name           Number         Value          Unit           mRID
  -------------- -------------- -------------- -------------- --------------------------------------
  Bus            1                             Integer        13D956D2-9975-461F-9BFF-B222E24302F4

  Model          2                             String         2BA9FFC4-0F2F-4E37-A5BB-E3F1114B177E

  ID             3              1              String         303094B6-477F-4B87-9C6F-7C9EA3A744B2

  BUSR           4                                            D488032D-90AB-49BE-9FEA-62096C4B2983

  BUS1           5                                            3A93999C-81B8-4B11-874B-E716310D1E61

  BUS2           6                                            DDD70F88-374A-4FD5-B53F-1DE139C5748E

  CKTID          7                                            C388E5B3-C823-4BD9-ACC4-C14C2A73EE41

  VCFlag         8              True           Boolean        1B13F8F7-FAC3-4CF1-A61F-7B0BCB3CFE34

  RefFlag        9              True           Boolean        0047194F-6E80-4D0E-981F-E051363E7604

  Fflag          10             True           Boolean        0C287014-57C4-4414-BF79-E5E8BCFA3008

  Tfltr          11             0.02           Seconds        D0627E06-0E87-489A-97AF-07619C7B9A24

  Kp             12             10.0           PU             51034D10-D82D-4E1C-88B8-3F9E00D6534E

  Ki             13             5.0            PU             5BFD03A5-DC6C-4EF3-B44D-65F636D23AB0

  Tft            14             0.0            Seconds        585D0407-70FA-4EAE-B1B2-C1A442650402

  Tfv            15             0.08           Seconds        698732A1-D3FF-4CEA-8FFB-E36C115915F3

  Vfrz           16             0.35           PU             8B53DEF3-7E2D-4D14-A84D-9EEB59CDEC35

  Rc             17             0.0            PU             79C13399-8782-4240-87E0-63A423C6D699

  Xc             18             0.0            PU             4051A34B-2CCC-40A8-A6EA-3330982C0446

  Kc             19             0.02           PU             CAF12779-6345-4830-95B0-ABD44E712D49

  emax           20             999.0          PU             90FEE5A4-3651-4C27-81B3-A70359D3A3E7

  emin           21             -999.0         PU             985F6294-B8E5-48B4-A64E-AA63C6AC57AF

  dbd1           22             0.0            PU             9660C61E-12CD-44B2-9380-BD10E3BB0E23

  dbd2           23                                           BB2D4793-35E9-4C00-8EEA-A6A6B11B30D9

  Qmax           24             0.7            PU             76F0C938-726A-402A-9C84-3D1AA4E988A9

  Qmin           25             -0.7           PU             EDD06008-09DD-4068-891A-005F0DBB1158

  Kpg            26             0.1            PU             F89005C6-7659-428B-B288-59CCC4E77B6E

  Kig            27             0.05           PU             C36F0003-2385-43EA-9F33-5B0E048020FA

  Tp             28             0.03           Seconds        D5947D7C-F6C7-4445-80FB-0AC5AE647CA0

  fdbd1          29             -0.01          PU             89900F37-BDD3-4ECF-83BE-A4BEC189ABCC

  fdbd2          30             0.01           PU             71DA756B-08B1-487E-9487-3F009B4F2382

  femax          31             999.0          PU             84E383C7-8C63-4DC5-93E5-15545BFE4D0D

  femin          32             -999.0         PU             835A024D-3610-497B-9FFD-657345CD53B5

  Pmax           33             1.0            PU             FBF9F943-1E02-41A1-9F1D-4B81E9FA6B54

  Pmin           34             0.0            PU             5E3D7FC9-9857-4CC1-9AAC-CE4DC662651F

  Tg             35             0.08           Seconds        2F057E4B-2294-47CF-B756-F048E7519ECD

  Ddn            36             20.0           PU             0DC3D3E8-ED7F-4C95-8F43-9FA11A7551FF

  Dup            37             0.0            PU             979A2FDB-3C8C-41C6-9CFC-06997A727A00
  --------------------------------------------------------------------------------------------------

  : REPCA1 Parameters

### SEXS

**nameKind**: DYR

**modelKind**: excitationSystem

**statusKind**: prohibited

**description**: Legacy static exciter

**closestStandardModel**: ExcSEXS

**mRID**: 854A4288-2FB4-47F9-A194-395CF22DD4E8

  --------------------------------------------------------------------------------------------------
  Name           Number         Value          Unit           mRID
  -------------- -------------- -------------- -------------- --------------------------------------
  Bus            1                             Integer        5FEC78BC-65D5-49CE-9D30-EA7F3D225EEF

  Model          2                             String         8C11F175-B4E3-49A7-91C5-7396992785F8

  ID             3              1              String         A55C670D-7976-40C8-8A33-5A332070D53E

  TATB           4              0.1            Float          360A2A9E-48B2-49FA-83F5-5518A4E16F81

  TB             5              10.0           Seconds        1FAE8B08-8F08-4773-AD98-AB0360E820EF

  K              6              100.0          PU             1D4EF184-08B1-4633-BA51-0C3A121FDF94

  TE             7              0.05           Seconds        0FAB61D9-EF26-4BCB-94FE-A19CBE2F3945

  EMIN           8              -5.0           PU             8C71701D-5C80-4E16-A5DB-9356BCB91854

  EMAX           9              5.0            PU             87E5FD37-97F8-4DE7-B23E-C3EA78AFF8FF
  --------------------------------------------------------------------------------------------------

  : SEXS Parameters

### TGOV1

**nameKind**: DYR

**modelKind**: turbineGovernor

**statusKind**: allowed

**description**:

**closestStandardModel**: GovSteam0

**mRID**: F7BBFF29-107F-46E5-AF37-71341F6B1587

  --------------------------------------------------------------------------------------------------
  Name           Number         Value          Unit           mRID
  -------------- -------------- -------------- -------------- --------------------------------------
  Bus            1                             Integer        63D52583-E641-4473-B924-05D8AE95E110

  Model          2                             String         208D50BB-630F-48E4-95DF-F33425C54C09

  ID             3              1              String         8D2C99C3-CE5B-4651-B60B-0714E24CA39C

  R              4              0.05           PU             EF182868-4670-4271-9684-231C1ACDF593

  T1             5              0.5            Seconds        182F1C59-EB7B-4684-95CD-D50341E402BE

  VMAX           6              1.0            PU             419CEBED-8D72-4BAF-9BB1-BBD6404BE950

  VMIN           7              0.0            PU             50A2FF9E-C212-4431-AC6E-A9A6B9BF1A34

  T2             8              3.0            Seconds        A56F1152-553D-4EBA-B7C0-BA204365C510

  T3             9              10.0           Seconds        4BEAFB82-FFB3-4551-AA12-AE8D4BC09610

  Dt             10             0.0            PU             9C1B56C0-9371-45ED-8679-AA0C5E8E5CEC
  --------------------------------------------------------------------------------------------------

  : TGOV1 Parameters

### WTARA1

**nameKind**: DYR

**modelKind**: renewableEnergyResource

**statusKind**: allowed

**description**:

**closestStandardModel**: WeccWTGARA

**mRID**: 86604D1C-DB00-4E4C-9348-1E6D5FFFE060

  --------------------------------------------------------------------------------------------------
  Name           Number         Value          Unit           mRID
  -------------- -------------- -------------- -------------- --------------------------------------
  Bus            1                             Integer        F9CA8BEE-E97E-4771-8999-9219885382DF

  Model          2                             String         EABCD859-78EC-424B-B652-59EA87389E1E

  ID             3              1              String         B51CB8F2-E4DE-4C3D-94BA-6B138F7DC777

  Ka             4              0.01           PU             0B09C389-F0A5-4FB8-B802-7BD22FFDDD49

  theta0         5              0.0            AngleDegrees   F3C76E21-540E-4189-9FF5-BC9C3E3C05D7
  --------------------------------------------------------------------------------------------------

  : WTARA1 Parameters

### WTDTA1

**nameKind**: DYR

**modelKind**: renewableEnergyResource

**statusKind**: allowed

**description**:

**closestStandardModel**: WeccWTGTA

**mRID**: D988EC5E-7EF1-418F-9F69-96995339E4BE

  --------------------------------------------------------------------------------------------------
  Name           Number         Value          Unit           mRID
  -------------- -------------- -------------- -------------- --------------------------------------
  Bus            1                             Integer        4DFA7ED9-C478-41D1-9EFC-CBB5A5CAE4A7

  Model          2                             String         383E3FBE-18A6-4BB9-A142-6ED5CD55A622

  ID             3              1              String         375B2BD1-C09F-4DBE-B0AC-FBF886F806CE

  H              4                                            FCFCC2DE-CEA2-4F22-9D80-BAFA9504F29B

  DAMP           5                                            9666AC13-89F6-4C44-A210-FB1DE4F87240

  Htfrac         6                                            FE403C09-3419-43C0-821A-70AEE0A090EC

  Freq1          7                                            DC2A17B5-F42E-458B-B3FB-A23716A472D9

  Dshaft         8              1.5            PU             53487495-3E33-4BD4-925E-5FCF38B971A1
  --------------------------------------------------------------------------------------------------

  : WTDTA1 Parameters
