#include <boost/python.hpp>
#include <scale_check.h>

using namespace boost::python;

BOOST_PYTHON_MODULE(scale_check) {
  def("get_bad_scale_values", usd_utilities::get_bad_scale_values,
      R"(Find zero-element index in an attribute.

        Note:
            If the user's environment defines a
            USD_CPP_UTILITIES_SCALE_UPPER_BOUND variable, it is read as
            a float and used. Otherwise, 0.0001 is the fallback value.

        Args:
           attribute (:class:`pxr.Usd.Attribute`):
               The attribute to check for any index whose value is 0.

        Returns:
           list[int]: The found, bad indices, if any.
        )");
}
