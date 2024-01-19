import unittest
from xml_parser import ParseTree


class TestParseTree(unittest.TestCase):
    def test_extract_tags_doc_1(self):
        return
        """
        Testing a valid barebones XML file
        """
        xml_string = """
        <legalDocument>
            <title>Title of Document</title>
            <description>Description of Legal Matter</description>
            <author>Author Name</author>
            <creationDate></creationDate>
            <content>
                <section>
                    <sectionTitle>Introduction</sectionTitle>
                    <paragraph>This is the introductory paragraph of the legal document.</paragraph>
                </section>
                <section>
                    <sectionTitle>Background</sectionTitle>
                    <paragraph>The background section provides context to the legal matter.</paragraph>
                </section>
                <section>
                    <sectionTitle>Legal Analysis</sectionTitle>
                    <subSection>
                        <subSectionTitle>Analysis Part 1</subSectionTitle>
                        <paragraph>Details of the first part of the legal analysis. Creation date is January 22, 2022.</paragraph>
                    </subSection>
                    <subSection>
                        <subSectionTitle>Analysis Part 2</subSectionTitle>
                        <paragraph>Details of the second part of the legal analysis.</paragraph>
                    </subSection>
                </section>
                <section>
                    <sectionTitle>Conclusion</sectionTitle>
                    <paragraph>Concluding remarks and final thoughts on the legal matter.</paragraph>
                </section>
            </content>
        </legalDocument>
        """
        parseTreeObj = ParseTree(xml_string)
        parseTreeObj.build_tree()
        output = parseTreeObj.extract_tags()

        expected_output = {
            'title': 'Title of Document',
            'description': 'Description of Legal Matter',
            'author': 'Author Name',
            'xml_data': ['<title></title>', '<description></description>', '<author></author>', '<creationDate></creationDate>', '<sectionTitle></sectionTitle>', '<paragraph></paragraph>', '<section><sectionTitle></sectionTitle><paragraph></paragraph></section>', '<sectionTitle></sectionTitle>', '<paragraph></paragraph>', '<section><sectionTitle></sectionTitle><paragraph></paragraph></section>', '<sectionTitle></sectionTitle>', '<subSectionTitle></subSectionTitle>', '<paragraph></paragraph>', '<subSection><subSectionTitle></subSectionTitle><paragraph></paragraph></subSection>', '<subSectionTitle></subSectionTitle>', '<paragraph></paragraph>', '<subSection><subSectionTitle></subSectionTitle><paragraph></paragraph></subSection>', '<section><sectionTitle></sectionTitle><subSection><subSectionTitle></subSectionTitle><paragraph></paragraph></subSection><subSection><subSectionTitle></subSectionTitle><paragraph></paragraph></subSection></section>', '<sectionTitle></sectionTitle>', '<paragraph></paragraph>', '<section><sectionTitle></sectionTitle><paragraph></paragraph></section>', '<content><section><sectionTitle></sectionTitle><paragraph></paragraph></section><section><sectionTitle></sectionTitle><paragraph></paragraph></section><section><sectionTitle></sectionTitle><subSection><subSectionTitle></subSectionTitle><paragraph></paragraph></subSection><subSection><subSectionTitle></subSectionTitle><paragraph></paragraph></subSection></section><section><sectionTitle></sectionTitle><paragraph></paragraph></section></content>', '<legalDocument><title></title><description></description><author></author><creationDate></creationDate><content><section><sectionTitle></sectionTitle><paragraph></paragraph></section><section><sectionTitle></sectionTitle><paragraph></paragraph></section><section><sectionTitle></sectionTitle><subSection><subSectionTitle></subSectionTitle><paragraph></paragraph></subSection><subSection><subSectionTitle></subSectionTitle><paragraph></paragraph></subSection></section><section><sectionTitle></sectionTitle><paragraph></paragraph></section></content></legalDocument>'],
            'created_at': ''
        }
        print(expected_output['xml_data'])

        self.assertListEqual(
            output['xml_data'], expected_output['xml_data'], "Lists are not equal")

        del output['xml_data']
        del expected_output['xml_data']

        self.assertEqual(output, expected_output)

    def test_extract_tags_doc_2(self):
        return
        """
        Testing a valid legal document
        """
        xml_string = """
            <legalDocument>
                <description>Detailed Analysis of Contractual Obligations</description>
                <author>Jane Doe</author>
                <creationDate>2024-02-15</creationDate>
                <content>
                    <section>
                        <sectionTitle>Scope of Agreement</sectionTitle>
                        <paragraph>This section outlines the scope of the agreement.</paragraph>
                    </section>
                    <section>
                        <sectionTitle>Terms and Conditions</sectionTitle>
                        <paragraph>Terms and conditions governing the contractual relationship are discussed here.</paragraph>
                    </section>
                    <section>
                        <sectionTitle>Rights and Responsibilities</sectionTitle>
                        <subSection>
                            <subSectionTitle>Party A's Rights</subSectionTitle>
                            <paragraph>Details of the rights held by Party A.</paragraph>
                        </subSection>
                        <subSection>
                            <subSectionTitle>Party B's Responsibilities</subSectionTitle>
                            <paragraph>Details of the responsibilities of Party B.</paragraph>
                        </subSection>
                    </section>
                    <section>
                        <sectionTitle>Dispute Resolution</sectionTitle>
                        <paragraph>This section describes the methods for dispute resolution.</paragraph>
                    </section>
                    <section>
                        <sectionTitle>Final Provisions</sectionTitle>
                        <paragraph>Concluding provisions and legal stipulations.</paragraph>
                    </section>
                </content>
            </legalDocument>
        """
        parseTreeObj = ParseTree(xml_string)
        parseTreeObj.build_tree()
        output = parseTreeObj.extract_tags()

        expected_output = {
            'description': 'Detailed Analysis of Contractual Obligations',
            'title': None,
            'author': 'Jane Doe',
            'xml_data': ['<description></description>', '<author></author>', '<creationDate></creationDate>', '<sectionTitle></sectionTitle>', '<paragraph></paragraph>', '<section><sectionTitle></sectionTitle><paragraph></paragraph></section>', '<sectionTitle></sectionTitle>', '<paragraph></paragraph>', '<section><sectionTitle></sectionTitle><paragraph></paragraph></section>', '<sectionTitle></sectionTitle>', '<subSectionTitle></subSectionTitle>', '<paragraph></paragraph>', '<subSection><subSectionTitle></subSectionTitle><paragraph></paragraph></subSection>', '<subSectionTitle></subSectionTitle>', '<paragraph></paragraph>', '<subSection><subSectionTitle></subSectionTitle><paragraph></paragraph></subSection>', '<section><sectionTitle></sectionTitle><subSection><subSectionTitle></subSectionTitle><paragraph></paragraph></subSection><subSection><subSectionTitle></subSectionTitle><paragraph></paragraph></subSection></section>', '<sectionTitle></sectionTitle>', '<paragraph></paragraph>', '<section><sectionTitle></sectionTitle><paragraph></paragraph></section>', '<sectionTitle></sectionTitle>', '<paragraph></paragraph>', '<section><sectionTitle></sectionTitle><paragraph></paragraph></section>', '<content><section><sectionTitle></sectionTitle><paragraph></paragraph></section><section><sectionTitle></sectionTitle><paragraph></paragraph></section><section><sectionTitle></sectionTitle><subSection><subSectionTitle></subSectionTitle><paragraph></paragraph></subSection><subSection><subSectionTitle></subSectionTitle><paragraph></paragraph></subSection></section><section><sectionTitle></sectionTitle><paragraph></paragraph></section><section><sectionTitle></sectionTitle><paragraph></paragraph></section></content>', '<legalDocument><description></description><author></author><creationDate></creationDate><content><section><sectionTitle></sectionTitle><paragraph></paragraph></section><section><sectionTitle></sectionTitle><paragraph></paragraph></section><section><sectionTitle></sectionTitle><subSection><subSectionTitle></subSectionTitle><paragraph></paragraph></subSection><subSection><subSectionTitle></subSectionTitle><paragraph></paragraph></subSection></section><section><sectionTitle></sectionTitle><paragraph></paragraph></section><section><sectionTitle></sectionTitle><paragraph></paragraph></section></content></legalDocument>'],
            'created_at': '2024-02-15'
        }
        print(expected_output['xml_data'])

        self.assertListEqual(
            output['xml_data'], expected_output['xml_data'], "Lists are not equal")

        del output['xml_data']
        del expected_output['xml_data']

        self.assertEqual(output, expected_output)

    def test_extract_tags_doc_3(self):
        return
        """
        Testing an valid legal document -- signatureBlock, exhibit, and section are self-closing
        """
        xml_string = """
         <legalDocument>
            <title>Settlement Agreement</title>
            <description>Outline of Settlement Terms</description>
            <author></author>
            <creationDate></creationDate>
            <content>
                <section>
                    <sectionTitle>Nature of Dispute</sectionTitle>
                    <paragraph>This section describes the nature of the dispute.</paragraph>
                    <exhibit/>
                </section>
                <section>
                    <sectionTitle>Settlement Terms</sectionTitle>
                    <subSection>
                        <subSectionTitle>Financial Terms</subSectionTitle>
                        <paragraph>Details of the financial settlement terms.</paragraph>
                    </subSection>
                    <subSection>
                        <subSectionTitle>Non-Disclosure Agreement</subSectionTitle>
                        <paragraph>Conditions regarding the confidentiality of the settlement.</paragraph>
                        <attachment/>
                    </subSection>
                </section>
                <section>
                    <sectionTitle>Effectiveness</sectionTitle>
                    <paragraph>This section explains when the settlement becomes effective. Just because there is a date here 2022-05-05, doesn't mean that this is the creation date.</paragraph>
                    <signatureBlock />
                </section>
                <section/>
            </content>
        </legalDocument>
            """
        parseTreeObj = ParseTree(xml_string)
        parseTreeObj.build_tree()
        output = parseTreeObj.extract_tags()

        expected_output = {
            'description': 'Outline of Settlement Terms',
            'title': 'Settlement Agreement',
            'author': None,
            'xml_data': ['<title></title>', '<description></description>', '<author></author>', '<creationDate></creationDate>', '<sectionTitle></sectionTitle>', '<paragraph></paragraph>', '<exhibit/>', '<sectionTitle></sectionTitle>', '<subSectionTitle></subSectionTitle>', '<paragraph></paragraph>', '<subSection><subSectionTitle></subSectionTitle><paragraph></paragraph></subSection>', '<subSectionTitle></subSectionTitle>', '<paragraph></paragraph>', '<attachment/>', '<subSection><subSectionTitle></subSectionTitle><paragraph></paragraph><attachment/></subSection>', '<sectionTitle></sectionTitle>', '<paragraph></paragraph>', '<signatureBlock/>', '<section/>', '<section><sectionTitle></sectionTitle><paragraph></paragraph><signatureBlock/><section/></section>', '<section><sectionTitle></sectionTitle><subSection><subSectionTitle></subSectionTitle><paragraph></paragraph></subSection><subSection><subSectionTitle></subSectionTitle><paragraph></paragraph><attachment/></subSection><section><sectionTitle></sectionTitle><paragraph></paragraph><signatureBlock/><section/></section></section>', '<section><sectionTitle></sectionTitle><paragraph></paragraph><exhibit/><section><sectionTitle></sectionTitle><subSection><subSectionTitle></subSectionTitle><paragraph></paragraph></subSection><subSection><subSectionTitle></subSectionTitle><paragraph></paragraph><attachment/></subSection><section><sectionTitle></sectionTitle><paragraph></paragraph><signatureBlock/><section/></section></section></section>', '<content><section><sectionTitle></sectionTitle><paragraph></paragraph><exhibit/><section><sectionTitle></sectionTitle><subSection><subSectionTitle></subSectionTitle><paragraph></paragraph></subSection><subSection><subSectionTitle></subSectionTitle><paragraph></paragraph><attachment/></subSection><section><sectionTitle></sectionTitle><paragraph></paragraph><signatureBlock/><section/></section></section></section></content>', '<legalDocument><title></title><description></description><author></author><creationDate></creationDate><content><section><sectionTitle></sectionTitle><paragraph></paragraph><exhibit/><section><sectionTitle></sectionTitle><subSection><subSectionTitle></subSectionTitle><paragraph></paragraph></subSection><subSection><subSectionTitle></subSectionTitle><paragraph></paragraph><attachment/></subSection><section><sectionTitle></sectionTitle><paragraph></paragraph><signatureBlock/><section/></section></section></section></content></legalDocument>'],
            'created_at': None
        }
        print(expected_output['xml_data'])

        self.assertListEqual(
            output['xml_data'], expected_output['xml_data'], "Lists are not equal")

        del output['xml_data']
        del expected_output['xml_data']

        self.assertEqual(output, expected_output)

    def test_extract_tags_doc_4(self):
        return
        """
        Testing an valid legal document -- has a lot of inline tags, is complex and tags have attributes
        """
        xml_string = """
        <legalDocument>
            <header>
                <title>Complex Legal Document</title>
                <meta>
                    <author>John Smith</author>
                    <co-author>Emily Johnson</co-author>
                    <creationDate>2024-04-01</creationDate>
                </meta>
            </header>
            <body>
                <section id="1">
                    <title>Introduction</title>
                    <content>Overview of the document's purpose.</content>
                    <note>Some notes <highlight>with <b>mixed</b> formatting</highlight> inside.</note>
                </section>
                <section id="2">
                    <title>Background</title>
                    <content>
                        <paragraph>Background information with <inlineTag>various</inlineTag> inline elements.</paragraph>
                        <list>
                            <item>Point 1</item>
                            <item>Point 2 with <b>bold</b> text</item>
                        </list>
                    </content>
                </section>
                <content>
                    <mixedContent>
                        This is <b>mixed</b> content outside a <normalTag>regular tag structure</normalTag>.
                        <moreContent>
                            More nested content with <a href="http://example.com">links</a> and other elements.
                        </moreContent>
                    </mixedContent>
                </content>
                <section id="3">
                    <title>Conclusion</title>
                    <content>
                        <conclusion>
                            Final thoughts and <unusualTag>remarks</unusualTag>.
                        </conclusion>
                    </content>
                    <attachments>
                        <file>attachment1.pdf</file>
                        <file>attachment2.jpg</file>
                        <file>attachment3.docx</file>
                    </attachments>
                </section>
            </body>
            <footer>
                <comments>
                    <comment>First comment</comment>
                    <comment>Second comment with <b>bold</b> text</comment>
                </comments>
            </footer>
        </legalDocument>
            """
        parseTreeObj = ParseTree(xml_string)
        parseTreeObj.build_tree()
        output = parseTreeObj.extract_tags()

        expected_output = {
            'description': None,
            'title': 'Complex Legal Document',
            'author': "John Smith",
            'xml_data': ['<title></title>', '<description></description>', '<author></author>', '<creationDate></creationDate>', '<sectionTitle></sectionTitle>', '<paragraph></paragraph>', '<exhibit/>', '<sectionTitle></sectionTitle>', '<subSectionTitle></subSectionTitle>', '<paragraph></paragraph>', '<subSection><subSectionTitle></subSectionTitle><paragraph></paragraph></subSection>', '<subSectionTitle></subSectionTitle>', '<paragraph></paragraph>', '<attachment/>', '<subSection><subSectionTitle></subSectionTitle><paragraph></paragraph><attachment/></subSection>', '<sectionTitle></sectionTitle>', '<paragraph></paragraph>', '<signatureBlock/>', '<section/>', '<section><sectionTitle></sectionTitle><paragraph></paragraph><signatureBlock/><section/></section>', '<section><sectionTitle></sectionTitle><subSection><subSectionTitle></subSectionTitle><paragraph></paragraph></subSection><subSection><subSectionTitle></subSectionTitle><paragraph></paragraph><attachment/></subSection><section><sectionTitle></sectionTitle><paragraph></paragraph><signatureBlock/><section/></section></section>', '<section><sectionTitle></sectionTitle><paragraph></paragraph><exhibit/><section><sectionTitle></sectionTitle><subSection><subSectionTitle></subSectionTitle><paragraph></paragraph></subSection><subSection><subSectionTitle></subSectionTitle><paragraph></paragraph><attachment/></subSection><section><sectionTitle></sectionTitle><paragraph></paragraph><signatureBlock/><section/></section></section></section>', '<content><section><sectionTitle></sectionTitle><paragraph></paragraph><exhibit/><section><sectionTitle></sectionTitle><subSection><subSectionTitle></subSectionTitle><paragraph></paragraph></subSection><subSection><subSectionTitle></subSectionTitle><paragraph></paragraph><attachment/></subSection><section><sectionTitle></sectionTitle><paragraph></paragraph><signatureBlock/><section/></section></section></section></content>', '<legalDocument><title></title><description></description><author></author><creationDate></creationDate><content><section><sectionTitle></sectionTitle><paragraph></paragraph><exhibit/><section><sectionTitle></sectionTitle><subSection><subSectionTitle></subSectionTitle><paragraph></paragraph></subSection><subSection><subSectionTitle></subSectionTitle><paragraph></paragraph><attachment/></subSection><section><sectionTitle></sectionTitle><paragraph></paragraph><signatureBlock/><section/></section></section></section></content></legalDocument>'],
            'created_at': "2024-04-01"
        }
        print(expected_output['xml_data'])

        self.assertListEqual(
            output['xml_data'], expected_output['xml_data'], "Lists are not equal")

        del output['xml_data']
        del expected_output['xml_data']

        self.assertEqual(output, expected_output)

    def test_extract_tags_doc_5(self):
        """
        Testing an valid legal document -- it has comments
        """
        xml_string = """
            <legalDocument>
                <header>
                    <title></title> <!-- Empty title -->
                    <meta>
                        <author>Author: Jane Doe</author>
                        <creationDate></creationDate> <!-- Missing creation date -->
                    </meta>
                </header>
                <body>
                    <section>
                        <title>Background</title>
                        <!-- Missing content section -->
                        <undefinedTag>Some undefined content</undefinedTag>
                    </section>
                    <ambiguous>
                        <content>Initial <b>content</b> with <i>tags</i></content>
                        <content> <!-- Nested content tags with missing information -->
                            <subContent></subContent> <!-- Empty subcontent -->
                            More text here
                            <subContent>
                                <p>Paragraph inside subcontent</p>
                            </subContent>
                        </content>
                        <undefinedStructure>
                            Irregular formatting and structure
                            <randomTag>Random information</randomTag>
                        </undefinedStructure>
                    </ambiguous>
                    <conclusion>
                        <summary>
                            <point>This is a summary point</point>
                            <!-- Missing summary point -->
                        </summary>
                        <finalThoughts></finalThoughts> <!-- Empty final thoughts -->
                    </conclusion>
                </body>
                <attachments>
                    <file>attachment1.pdf</file>
                    <!-- Missing file tag -->
                    <file>attachment3.docx</file>
                </attachments>
                <!-- Missing footer -->
            </legalDocument>
                """
        parseTreeObj = ParseTree(xml_string)
        parseTreeObj.build_tree()
        output = parseTreeObj.extract_tags()

        expected_output = {
            'description': None,
            'title': None,
            'author': "Author: Jane Doe",
            'xml_data': ['<title></title>', '<author></author>', '<creationDate></creationDate>', '<meta><author></author><creationDate></creationDate></meta>', '<header><title></title><meta><author></author><creationDate></creationDate></meta></header>', '<title></title>', '<undefinedTag></undefinedTag>', '<section><title></title><undefinedTag></undefinedTag></section>', '<b></b>', '<i></i>', '<content><b></b><i></i></content>', '<subContent></subContent>', '<p></p>', '<subContent><p></p></subContent>', '<content><subContent></subContent><subContent><p></p></subContent></content>', '<randomTag></randomTag>', '<undefinedStructure><randomTag></randomTag></undefinedStructure>', '<ambiguous><content><b></b><i></i></content><content><subContent></subContent><subContent><p></p></subContent></content><undefinedStructure><randomTag></randomTag></undefinedStructure></ambiguous>', '<point></point>', '<summary><point></point></summary>', '<finalThoughts></finalThoughts>', '<conclusion><summary><point></point></summary><finalThoughts></finalThoughts></conclusion>', '<body><section><title></title><undefinedTag></undefinedTag></section><ambiguous><content><b></b><i></i></content><content><subContent></subContent><subContent><p></p></subContent></content><undefinedStructure><randomTag></randomTag></undefinedStructure></ambiguous><conclusion><summary><point></point></summary><finalThoughts></finalThoughts></conclusion></body>', '<file></file>', '<file></file>', '<attachments><file></file><file></file></attachments>', '<legalDocument><header><title></title><meta><author></author><creationDate></creationDate></meta></header><body><section><title></title><undefinedTag></undefinedTag></section><ambiguous><content><b></b><i></i></content><content><subContent></subContent><subContent><p></p></subContent></content><undefinedStructure><randomTag></randomTag></undefinedStructure></ambiguous><conclusion><summary><point></point></summary><finalThoughts></finalThoughts></conclusion></body><attachments><file></file><file></file></attachments></legalDocument>'],
            'created_at': None
        }
        print(expected_output['xml_data'])

        self.assertListEqual(
            output['xml_data'], expected_output['xml_data'], "Lists are not equal")

        del output['xml_data']
        del expected_output['xml_data']

        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()
